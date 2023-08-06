import typer
from pathlib import Path
from typing import Optional
import anyio
import httpx
from rich.console import Console
from rich.progress import Progress, TaskID
import nest_asyncio
nest_asyncio.apply()

images_app = typer.Typer()

console = Console()

#Images retrieval code adapted from: https://lewoudar.medium.com/click-a-beautiful-python-library-to-write-cli-applications-9c8154847066

def get_image_urls(path):
    images = []
    p = Path(path)
    with p.open() as f:
        for line in f:
            line = line.strip(' \n')
            if not line:
                continue
            images.append(line)
    return images

async def download_image(progress, task_id, image_url, destination):
    async with httpx.AsyncClient() as client:
        response = await client.get(image_url)
        if response.status_code >= 400:
            progress.console.print(f'image [blue]{image_url}[/] could not be downloaded')
            progress.update(task_id, advance=1)
            return

        path = destination / (image_url.split('/')[-1])
        path.write_bytes(response.content)
        progress.update(task_id, advance=1)


async def worker(image_urls, progress, task_id, destination):
    async with anyio.create_task_group() as tg:
        for image_url in image_urls:
            await tg.spawn(download_image, progress, task_id, image_url, destination)

@images_app.command()
def get_images(input_file: Optional[Path] = typer.Option(..., help="Text file containing all URLs splited by line"), output_folder: Optional[Path] = typer.Option(..., help="Folder path where the images will be stored")):
    """
    Get all images from a text file (in Async mode)
    """
    if input_file is None:
        typer.echo("URLs text file not found!")
        raise typer.Abort()

    if not output_folder.is_dir():
        typer.echo("Folder not found!")
        raise typer.Abort()

    if input_file.is_file() and output_folder.is_dir():
        image_urls = get_image_urls(input_file)
        with Progress(console=console) as progress:
            task_id = progress.add_task('Downloading', total=len(image_urls))
            anyio.run(worker, image_urls, progress, task_id, output_folder)
        console.print('All images downloaded!')
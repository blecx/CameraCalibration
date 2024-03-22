import argparse
from typing import Any, Optional

from reportlab.lib.pagesizes import A4, mm
from reportlab.lib.units import mm
from reportlab.pdfgen import canvas


def draw_square(
    canvas: canvas.Canvas, x: int, y: int, square_size: int, fill: bool = True
) -> None:
    """Draws a square on the given canvas at the specified coordinates.

    Args:
        canvas (canvas.Canvas): The canvas to draw on.
        x (int): The x-coordinate of the square.
        y (int): The y-coordinate of the square.
        square_size (int): The size of the square in millimeters.
        fill (bool, optional): Whether to fill the square with color. Defaults to True.
    """
    if fill:
        canvas.rect(x, y, square_size, square_size, fill=1)
    else:
        canvas.rect(x, y, square_size, square_size, stroke=1)


def draw_chessboard(
    canvas: canvas.Canvas, num_rows: int, num_cols: int, square_size: int = 20
) -> None:
    """Draws a chessboard pattern on the given canvas.

    Args:
        canvas (canvas.Canvas): The canvas to draw on.
        num_rows (int): The number of rows in the chessboard pattern.
        num_cols (int): The number of columns in the chessboard pattern.
        square_size (int, optional): The size of the squares in the chessboard pattern. Defaults to 20.
    """
    for row in range(num_rows):
        for col in range(num_cols):
            if (row + col) % 2 == 0:
                fill = True
            else:
                fill = False
            draw_square(canvas, col * square_size, row *
                        square_size, square_size, fill)


def generate_pdf(
    file_name: str, num_rows: int, num_cols: int, square_size: Optional[int] = 20
) -> None:
    """Creates a PDF file with a chessboard pattern.

    Args:
        file_name (str): The name of the PDF file to create.
        num_rows (int): The number of rows in the chessboard pattern.
        num_cols (int): The number of columns in the chessboard pattern.
        square_size (int, optional): The size of the squares in the chessboard pattern. Defaults to 20.
    """
    if num_rows <= 0 or num_cols <= 0:
        raise ValueError(
            "Number of rows and columns must be greater than zero.")

    c = canvas.Canvas(file_name, pagesize=A4)
    draw_chessboard(c, num_rows, num_cols, square_size)
    c.save()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Generate a chessboard pattern in PDF format."
    )
    parser.add_argument("-r", "--rows", type=int, default=6,
                        help="Number of squares in a row (default: 6)")
    parser.add_argument("-c", "--columns", type=int, default=9,
                        help="Number of squares in a column (default: 9)")
    parser.add_argument("-s", "--size", type=int, default=20,
                        help="Size of the checker pattern in mm (default: 20)")
    parser.add_argument("-f", "--file", default="chessboardDefaultPattern.pdf",
                        help="Name of the file to store the pattern (default: chessboardDefaultPattern.pdf)")
    parser.add_argument("-h", "--help", action="help",
                        help="Show this help message and exit.")

    args = parser.parse_args()

    generate_pdf(args.file, args.rows, args.columns, args.size)


from fastmcp import FastMCP
import random

mcp = FastMCP("RandomNumberServer")


@mcp.tool()
def generate_random_number(min_value: int = 1, max_value: int = 100) -> int:
    """Generate a random integer between the minimum and maximum values."""
    return random.randint(min_value, max_value)


@mcp.tool()
def generate_random_numbers(count: int = 5, min_value: int = 1, max_value: int = 100) -> list[int]:
    """Generate multiple random integers within a specified range."""
    return [
        random.randint(min_value, max_value)
        for _ in range(count)
    ]


@mcp.tool()
def roll_dice() -> int:
    """Roll a standard six-sided dice and return a number from 1 to 6."""
    return random.randint(1, 6)


if __name__ == "__main__":
    mcp.run(transport='http',port = '8000')

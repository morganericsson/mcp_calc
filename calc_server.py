from mcp.server.fastmcp import FastMCP

app = FastMCP(
    title="Simple Calculator",
    description="A server to do simple calculations",
    version="0.1",
)


@app.tool()
def add(v1: int, v2: int) -> int:
    """
    Adds to integers and returns the result
    """

    return v1 + v2


@app.tool()
def subtract(v1: int, v2: int) -> int:
    """
    Subtracts v2 from v1 and returns the result
    """

    return v1 - v2


if __name__ == "__main__":
    app.run()

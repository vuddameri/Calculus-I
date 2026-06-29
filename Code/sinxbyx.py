import marimo

__generated_with = "0.23.11"
app = marimo.App(width="medium")


@app.cell(hide_code=True)
def _():
    import marimo as mo
    import numpy as np
    import matplotlib.pyplot as plt

    return mo, np, plt


@app.cell(hide_code=True)
def _(mo):
    x_slider = mo.ui.slider(
        start=-2.0,
        stop=2.0,
        step=0.01,
        value=1.0,
        label="x (radians)"
    )
    x_slider
    return (x_slider,)


@app.cell(hide_code=True)
def _(np, plt, x_slider):
    x = np.linspace(-10, 10, 1000)

    # Compute sin(x)/x safely
    y = np.where(np.abs(x) < 1e-10, 1.0, np.sin(x)/x)

    xv = x_slider.value
    if abs(xv) < 1e-10:
        yv = 1.0
    else:
        yv = np.sin(xv)/xv

    fig, ax = plt.subplots(figsize=(8,5))

    ax.plot(x, y, linewidth=2, label=r"$\sin(x)/x$")
    ax.scatter(xv, yv, color="red", s=80, zorder=5)
    ax.scatter(0,1,color="black",s=90)

    ax.axhline(1, color="gray", linestyle="--", alpha=0.6)
    ax.axvline(0, color="gray", linestyle="--", alpha=0.6)

    ax.set_xlim(-10, 10)
    ax.set_ylim(-0.4, 1.2)

    ax.set_xlabel("x (radians)")
    ax.set_ylabel(r"$\sin(x)/x$")
    ax.set_title(r"Interactive Exploration of $\sin(x)/x$")

    ax.grid(True)

    plt.show()
    return


if __name__ == "__main__":
    app.run()

import marimo

__generated_with = "0.23.11"
app = marimo.App()


@app.cell(hide_code=True)
def _():
    import marimo as mo
    import numpy as np
    import matplotlib.pyplot as plt

    return mo, np, plt


@app.cell(hide_code=True)
def _(mo):
    time = mo.ui.slider(
        start=0,
        stop=15,
        step=0.05,
        value=5,
        label="Time"
    )

    amplitude = mo.ui.slider(
        start=0.5,
        stop=20,
        step=0.1,
        value=2,
        label="Amplitude"
    )

    mo.vstack([time, amplitude])
    return amplitude, time


@app.cell(hide_code=True)
def _(amplitude, np, plt, time):
    t = time.value
    A = amplitude.value

    x = np.linspace(0, 15, 400)

    y = A * np.sin(x)

    y0 = A * np.sin(t)
    yp = A * np.cos(t)

    tangent = y0 + yp * (x - t)

    fig, ax = plt.subplots(figsize=(8, 4))

    ax.plot(x, y, lw=2)
    ax.plot(x, tangent, "r--", lw=2)

    ax.scatter(
        t,
        y0,
        s=120,
        facecolor="white",
        edgecolor="black",
        zorder=10
    )

    ax.set_xlabel("time")
    ax.set_ylabel("Height")
    ax.grid(True)

    print(f"f(t)   = {y0:.3f}")
    print(f"f'(t)  = {yp:.3f}")

    fig
    return


if __name__ == "__main__":
    app.run()

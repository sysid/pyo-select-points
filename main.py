import logging
import time

import helper
import settings
import typer
import pandas as pd

from sched_machine2 import SchedMachine2

_log = logging.getLogger(__name__)

app = typer.Typer()


@app.command()
def run(ctx: typer.Context, name: str, save: bool = False, verbose: bool = False):
    _log.info(f"Running configuration: {name}")

    config = getattr(settings, name)

    m = select-points(name=name, config=config)

    m.save_model()
    m.solve(tee=False, keepfiles=False)
    m.save_model()

    if m.is_solved:
        m.save_dill()
        m.show()
        if save:
            m.plot(save=f'{name}.png')
        else:
            m.plot()


@app.callback()
def main(ctx: typer.Context):
    """
    Optimization energy transactions
    """
    typer.echo(f"About to execute command: {ctx.invoked_subcommand}")


if __name__ == "__main__":
    log_fmt = r"%(asctime)-15s %(levelname)s %(name)s %(funcName)s:%(lineno)d %(message)s"
    logging.basicConfig(format=log_fmt, level=logging.DEBUG)
    logging.getLogger('matplotlib').setLevel(logging.INFO)
    print(f"{'select-points':.^80}")


    app(obj=dict(xxx="xxx"))

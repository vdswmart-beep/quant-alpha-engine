import subprocess


def run_dashboard():

    subprocess.run(

        [
            "streamlit",
            "run",
            "dashboard/research/app.py"
        ]

    )


if __name__ == "__main__":

    run_dashboard()
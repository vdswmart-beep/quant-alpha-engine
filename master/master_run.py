from master.run_research import run_research
from master.run_portfolio import run_portfolio


def main():

    print("\n========== RESEARCH ==========\n")
    run_research()

    print("\n========== PORTFOLIO ==========\n")
    run_portfolio()

    print("\nDONE\n")


if __name__ == "__main__":
    main()
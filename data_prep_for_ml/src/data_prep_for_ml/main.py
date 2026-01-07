import argparse
from databricks.sdk.runtime import spark
from data_prep_for_ml import taxis


def main():
    # Example: just find all taxis from a sample catalog
    taxis.find_all_taxis().show(5)


if __name__ == "__main__":
    main()

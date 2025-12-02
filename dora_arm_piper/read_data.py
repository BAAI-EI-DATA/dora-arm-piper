import logging_mp
from dora import Node


logger = logging_mp.get_logger(__name__)

node = Node()

def main():
    for event in node:
        if event["type"] == "INPUT":
            if "jointstate" in event["id"]:
                data = event["value"].to_numpy()
                logger.info(f"Dora node recieved dataflow \"{event["id"]}\": \n{data}")

        if event["type"] == "STOP":
            break

if __name__ == "__main__":
    main()
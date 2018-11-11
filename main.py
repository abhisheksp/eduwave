import argparse
from datetime import datetime

from pythonosc import osc_server
from pythonosc import dispatcher

from database import save_concentration


def create_concentration_entry(concentration):
    return {
        'current_timestamp': datetime.utcnow(),
        'concentration': concentration,
    }


def concentration_handler(unused_addr, args, concentration):
    print("Concentration: ", concentration)
    save_concentration(create_concentration_entry(concentration))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip",
                        default="127.0.0.1",
                        help="The ip to listen on")
    parser.add_argument("--port",
                        type=int,
                        default=5000,
                        help="The port to listen on")
    args = parser.parse_args()
    dispatcher = dispatcher.Dispatcher()
    dispatcher.map("/debug", print)
    dispatcher.map("/muse/elements/experimental/concentration", concentration_handler, "Concentration")

    server = osc_server.ThreadingOSCUDPServer(
        (args.ip, args.port), dispatcher)
    print("Serving on {}".format(server.server_address))
    server.serve_forever()

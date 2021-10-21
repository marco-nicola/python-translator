# Copyright 2021 Marco Nicola
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import argparse
import logging
from concurrent import futures

import grpc
from .config import Config
from .models_manager import ModelsManager
from .servicer import Servicer

from .grpcapi import api_pb2_grpc


def main() -> None:
    parser = argparse.ArgumentParser(description='Run the translator server.')
    parser.add_argument('-c', '--config', dest='config', required=True,
                        help='path to YAML configuration file')
    args = parser.parse_args()

    config = Config.from_yaml_file(args.config)

    logging.basicConfig(
        format='%(asctime)s %(levelname)s %(message)s',
        level=config.log_level)

    manager = ModelsManager(config)
    manager.load_models()

    servicer = Servicer(manager)

    server = grpc.server(futures.ThreadPoolExecutor(
        max_workers=config.max_workers))

    api_pb2_grpc.add_ApiServicer_to_server(servicer, server)
    address = f'{config.host}:{config.port}'
    server.add_insecure_port(address)
    logging.info(f'serving on {address}')
    server.start()

    try:
        server.wait_for_termination()
    except KeyboardInterrupt:
        logging.info('KeyboardInterrupt')

    logging.info('Bye!')


if __name__ == '__main__':
    main()

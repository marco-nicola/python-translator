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

from dataclasses import dataclass
import yaml


@dataclass
class ConfigLanguageModel:
    source: str
    target: str
    model: str


@dataclass
class Config:
    log_level: str
    host: str
    port: int
    max_workers: int
    models_path: str
    language_models: list[ConfigLanguageModel]

    @staticmethod
    def from_yaml_file(file: str) -> 'Config':
        with open(file, 'r') as f:
            data = yaml.safe_load(f)
        return Config(
            log_level=data['log_level'],
            host=data['host'],
            port=data['port'],
            max_workers=data['max_workers'],
            models_path=data['models_path'],
            language_models=[
                ConfigLanguageModel(
                    source=lm['source'],
                    target=lm['target'],
                    model=lm['model'],
                )
                for lm in data['language_models']
            ]
        )

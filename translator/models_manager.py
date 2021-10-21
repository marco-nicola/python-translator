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

import logging
from typing import Optional

from .config import Config, ConfigLanguageModel
from .model import Model


class ModelNotFound(Exception):
    pass


class ModelsManager:
    def __init__(self, config: Config):
        self._config: Config = config
        self._models: dict[str, dict[str, Model]] = dict()

    def load_models(self) -> None:
        logging.info(f'Loading all models...')

        for lm in self._config.language_models:
            self._load_model(lm)

        logging.info(f'All models loaded...')

    def translate(self, source: str, target: str, text: str) -> str:
        model = self._get_model(source, target)
        if not model:
            raise ModelNotFound(f'no model for "{source}" to "{target}"')
        return model.translate(text)

    def _get_model(self, source: str, target: str) -> Optional[Model]:
        if source in self._models and target in self._models[source]:
            return self._models[source][target]
        return None

    def _load_model(self, lm_conf: ConfigLanguageModel) -> None:
        source = lm_conf.source
        target = lm_conf.target

        if source not in self._models:
            self._models[source] = dict()

        if target in self._models[source]:
            raise Exception(f'model already loaded for "{source}" to "{target}"')

        model = Model(lm_conf, self._config.models_path)
        model.load()
        self._models[source][target] = model

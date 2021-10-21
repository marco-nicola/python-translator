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

from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, MarianMTModel, \
    MarianTokenizer

from .config import ConfigLanguageModel


class Model:
    def __init__(self, conf: ConfigLanguageModel, models_path: str):
        self._conf: ConfigLanguageModel = conf
        self._models_path: str = models_path
        self._tokenizer: Optional[MarianTokenizer] = None
        self._model: Optional[MarianMTModel] = None

    def load(self) -> None:
        logging.info(f'[{self._conf.model}] - Loading tokenizer...')
        self._tokenizer = AutoTokenizer.from_pretrained(
            self._conf.model, cache_dir=self._models_path)

        logging.info(f'[{self._conf.model}] - Loading model...')
        self._model = AutoModelForSeq2SeqLM.from_pretrained(
            self._conf.model, cache_dir=self._models_path)

        logging.info(f'[{self._conf.model}] - Loaded.')

    def translate(self, text: str) -> str:
        tokenized = self._tokenizer(text, return_tensors="pt", padding=True)
        outputs = self._model.generate(**tokenized)
        return self._tokenizer.decode(outputs[0], skip_special_tokens=True)

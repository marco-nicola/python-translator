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

from datetime import datetime

from .grpcapi import api_pb2, api_pb2_grpc
from .models_manager import ModelsManager, ModelNotFound


class Servicer(api_pb2_grpc.ApiServicer):
    def __init__(self, manager: ModelsManager):
        super().__init__()
        self._manager: ModelsManager = manager

    def TranslateText(self, request, context):
        source = request.translate_text_input.source_language
        target = request.translate_text_input.target_language
        text = request.translate_text_input.text

        data = None
        errors = None

        try:
            start_time = datetime.now()
            result = self._manager.translate(source, target, text)
            time_diff = datetime.now() - start_time
            data = api_pb2.TranslateTextData(
                took=time_diff.total_seconds(),
                translated_text=result
            )
        except ModelNotFound as ex:
            errors = api_pb2.ResponseErrors(
                value=[api_pb2.ResponseError(message=str(ex))]
            )

        return api_pb2.TranslateTextResponse(data=data, errors=errors)

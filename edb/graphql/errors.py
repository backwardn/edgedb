#
# This source file is part of the EdgeDB open source project.
#
# Copyright 2016-present MagicStack Inc. and the EdgeDB authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#


from edb import errors


from edb.common.exceptions import add_context


class GraphQLError(errors.QueryError):
    pass


class GraphQLTranslationError(GraphQLError):
    def __init__(self, msg, *, context=None):
        super().__init__(msg)

        if context:
            add_context(self, context)
            self._attrs['L'] = context.start.line
            self._attrs['C'] = context.start.column


class GraphQLValidationError(GraphQLTranslationError):
    pass


class GraphQLCoreError(GraphQLError):
    def __init__(self, msg, *, line=None, col=None):
        super().__init__(msg)

        if line:
            self._attrs['L'] = line
        if col:
            self._attrs['C'] = col
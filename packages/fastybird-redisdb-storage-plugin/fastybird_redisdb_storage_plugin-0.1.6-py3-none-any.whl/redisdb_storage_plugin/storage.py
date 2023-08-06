#!/usr/bin/python3

#     Copyright 2021. FastyBird s.r.o.
#
#     Licensed under the Apache License, Version 2.0 (the "License");
#     you may not use this file except in compliance with the License.
#     You may obtain a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#     Unless required by applicable law or agreed to in writing, software
#     distributed under the License is distributed on an "AS IS" BASIS,
#     WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#     See the License for the specific language governing permissions and
#     limitations under the License.

"""
Redis DB module
"""

# Python base dependencies
from typing import Dict, Optional, Tuple, Type, Union

# Library libs
from redisdb_storage_plugin.models import StorageManager, StorageRepository
from redisdb_storage_plugin.state import StorageItem


class StorageSettings:
    """
    Redis storage configuration

    @package        FastyBird:RedisDbStoragePlugin!
    @module         redis

    @author         Adam Kadlec <adam.kadlec@fastybird.com>
    """

    __host: str = "127.0.0.1"
    __port: int = 6379
    __username: Optional[str] = None
    __password: Optional[str] = None
    __database: int = 0

    # -----------------------------------------------------------------------------

    def __init__(self, config: Dict[str, Union[str, int, None]]) -> None:
        self.__host = str(config.get("host", "127.0.0.1")) if config.get("host", None) is not None else "127.0.0.1"
        self.__port = int(str(config.get("port", 6379)))
        self.__username = str(config.get("user", None)) if config.get("user", None) is not None else None
        self.__password = str(config.get("passwd", None)) if config.get("passwd", None) is not None else None
        self.__database = int(str(config.get("database", 0)))

    # -----------------------------------------------------------------------------

    @property
    def host(self) -> str:
        """Connection host"""
        return self.__host

    # -----------------------------------------------------------------------------

    @property
    def port(self) -> int:
        """Connection port"""
        return self.__port

    # -----------------------------------------------------------------------------

    @property
    def username(self) -> Optional[str]:
        """Connection username"""
        return self.__username

    # -----------------------------------------------------------------------------

    @property
    def password(self) -> Optional[str]:
        """Connection password"""
        return self.__password

    # -----------------------------------------------------------------------------

    @property
    def database(self) -> int:
        """Database number"""
        return self.__database


def define_models(
    config: Dict[str, Union[str, int, None]],
    entity: Type[StorageItem] = StorageItem,
) -> Tuple[StorageRepository, StorageManager]:
    """Initialize repository and manager"""
    settings: StorageSettings = StorageSettings(config)

    storage_repository = StorageRepository(
        host=settings.host,
        port=settings.port,
        database=settings.database,
        entity=entity,
    )
    storage_manager = StorageManager(
        host=settings.host,
        port=settings.port,
        storage_repository=storage_repository,
        database=settings.database,
        entity=entity,
    )

    return storage_repository, storage_manager

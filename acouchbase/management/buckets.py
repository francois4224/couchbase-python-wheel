from typing import (TYPE_CHECKING,
                    Any,
                    Awaitable,
                    List)

from acouchbase.management.logic import BucketMgmtWrapper
from couchbase.management.logic.buckets_logic import (BucketManagerLogic,
                                                      BucketSettings,
                                                      CreateBucketSettings)

if TYPE_CHECKING:
    from couchbase.management.options import (CreateBucketOptions,
                                              DropBucketOptions,
                                              FlushBucketOptions,
                                              GetAllBucketOptions,
                                              GetBucketOptions,
                                              UpdateBucketOptions)


class BucketManager(BucketManagerLogic):
    def __init__(self, connection, loop):
        super().__init__(connection)
        self._loop = loop

    @property
    def loop(self):
        """
        **INTERNAL**
        """
        return self._loop

    @BucketMgmtWrapper.inject_callbacks(None, BucketManagerLogic._ERROR_MAPPING)
    def create_bucket(self,
                      settings,  # type: CreateBucketSettings
                      *options,  # type: CreateBucketOptions
                      **kwargs   # type: Any
                      ) -> Awaitable[None]:
        """
        Creates a new bucket.

        :param: CreateBucketSettings settings: settings for the bucket.
        :param: CreateBucketOptions options: options for setting the bucket.
        :param: Any kwargs: override corresponding values in the options.

        :raises: BucketAlreadyExistsException
        :raises: InvalidArgumentsException
        """
        super().create_bucket(settings, *options, **kwargs)

    @BucketMgmtWrapper.inject_callbacks(None, BucketManagerLogic._ERROR_MAPPING)
    def update_bucket(self,
                      settings,  # type: BucketSettings
                      *options,  # type: UpdateBucketOptions
                      **kwargs  # type: Any
                      ) -> Awaitable[None]:

        super().update_bucket(settings, *options, **kwargs)

    @BucketMgmtWrapper.inject_callbacks(None, BucketManagerLogic._ERROR_MAPPING)
    def drop_bucket(self,
                    bucket_name,  # type: str
                    *options,     # type: DropBucketOptions
                    **kwargs      # type: Any
                    ) -> Awaitable[None]:

        super().drop_bucket(bucket_name, *options, **kwargs)

    @BucketMgmtWrapper.inject_callbacks(BucketSettings, BucketManagerLogic._ERROR_MAPPING)
    def get_bucket(self,
                   bucket_name,   # type: str
                   *options,      # type: GetBucketOptions
                   **kwargs       # type: Any
                   ) -> Awaitable[BucketSettings]:

        super().get_bucket(bucket_name, *options, **kwargs)

    @BucketMgmtWrapper.inject_callbacks(BucketSettings, BucketManagerLogic._ERROR_MAPPING)
    def get_all_buckets(self,
                        *options,  # type: GetAllBucketOptions
                        **kwargs  # type: Any
                        ) -> Awaitable[List[BucketSettings]]:

        super().get_all_buckets(*options, **kwargs)

    @BucketMgmtWrapper.inject_callbacks(None, BucketManagerLogic._ERROR_MAPPING)
    def flush_bucket(self,
                     bucket_name,   # type: str
                     *options,      # type: FlushBucketOptions
                     **kwargs       # type: Any
                     ) -> Awaitable[None]:

        super().flush_bucket(bucket_name, *options, **kwargs)
from twisted.internet.defer import Deferred

from couchbase.exceptions import (PYCBC_ERROR_MAP,
                                  AlreadyQueriedException,
                                  CouchbaseException,
                                  ErrorMapper,
                                  ExceptionMap)
from couchbase.exceptions import exception as CouchbaseBaseException
from couchbase.logic.views import ViewRequestLogic, ViewRow


class ViewRequest(ViewRequestLogic):
    def __init__(self,
                 connection,
                 loop,
                 encoded_query,
                 **kwargs
                 ):
        super().__init__(connection, encoded_query, **kwargs)
        self._query_request_ftr = None
        self._query_d = None
        self._loop = loop

    @property
    def loop(self):
        """
        **INTERNAL**
        """
        return self._loop

    @classmethod
    def generate_view_request(cls, connection, loop, encoded_query, **kwargs):
        return cls(connection, loop, encoded_query, **kwargs)

    def execute_view_query(self):
        # if self._query_request_ftr is not None and self._query_request_ftr.done():
        if self.done_streaming:
            raise AlreadyQueriedException()

        if self._query_request_ftr is None:
            self._query_request_ftr = self.loop.create_future()
            self._submit_query(callback=self._on_query_complete)
            self._query_d = Deferred.fromFuture(self._query_request_ftr)

        return self._query_d

    def _on_query_complete(self, result):
        print(f'_on_query_callback: {result}')
        self._loop.call_soon_threadsafe(self._query_request_ftr.set_result, result)

    def _get_metadata(self):
        try:
            view_response = next(self._streaming_result)
            self._set_metadata(view_response)
        except CouchbaseException as ex:
            raise ex
        except Exception as ex:
            exc_cls = PYCBC_ERROR_MAP.get(ExceptionMap.InternalSDKException.value, CouchbaseException)
            excptn = exc_cls(str(ex))
            raise excptn

    def __iter__(self):
        return self

    def _get_next_row(self):
        if self._done_streaming is True:
            return

        row = next(self._streaming_result)
        if isinstance(row, CouchbaseBaseException):
            raise ErrorMapper.build_exception(row)
        # should only be None one query request is complete and _no_ errors found
        if row is None:
            raise StopIteration

        # TODO:  until streaming, a dict is returned, no deserializing...
        # deserialized_row = self.serializer.deserialize(row)
        deserialized_row = row
        if issubclass(self.row_factory, ViewRow):
            return self.row_factory(**deserialized_row)
        else:
            return deserialized_row

    def __next__(self):
        try:
            return self._get_next_row()
        except StopIteration:
            self._done_streaming = True
            self._get_metadata()
            raise
        except CouchbaseException as ex:
            raise ex
        except Exception as ex:
            exc_cls = PYCBC_ERROR_MAP.get(ExceptionMap.InternalSDKException.value, CouchbaseException)
            excptn = exc_cls(str(ex))
            raise excptn

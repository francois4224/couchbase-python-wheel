from __future__ import annotations

from typing import (TYPE_CHECKING,
                    Any,
                    Dict,
                    List)

from couchbase.management.logic.eventing_logic import EventingFunctionBucketAccess  # noqa: F401
from couchbase.management.logic.eventing_logic import EventingFunctionBucketBinding  # noqa: F401
from couchbase.management.logic.eventing_logic import EventingFunctionConstantBinding  # noqa: F401
from couchbase.management.logic.eventing_logic import EventingFunctionDcpBoundary  # noqa: F401
from couchbase.management.logic.eventing_logic import EventingFunctionDeploymentStatus  # noqa: F401
from couchbase.management.logic.eventing_logic import EventingFunctionKeyspace  # noqa: F401
from couchbase.management.logic.eventing_logic import EventingFunctionLanguageCompatibility  # noqa: F401
from couchbase.management.logic.eventing_logic import EventingFunctionLogLevel  # noqa: F401
from couchbase.management.logic.eventing_logic import EventingFunctionProcessingStatus  # noqa: F401
from couchbase.management.logic.eventing_logic import EventingFunctionSettings  # noqa: F401
from couchbase.management.logic.eventing_logic import EventingFunctionState  # noqa: F401
from couchbase.management.logic.eventing_logic import EventingFunctionStatus  # noqa: F401
from couchbase.management.logic.eventing_logic import EventingFunctionUrlAuthBasic  # noqa: F401
from couchbase.management.logic.eventing_logic import EventingFunctionUrlAuthBearer  # noqa: F401
from couchbase.management.logic.eventing_logic import EventingFunctionUrlAuthDigest  # noqa: F401
from couchbase.management.logic.eventing_logic import EventingFunctionUrlBinding  # noqa: F401
from couchbase.management.logic.eventing_logic import EventingFunctionUrlNoAuth  # noqa: F401
from couchbase.management.logic.eventing_logic import (EventingFunction,
                                                       EventingFunctionManagerLogic,
                                                       EventingFunctionsStatus)
from couchbase.management.logic.wrappers import EventingFunctionMgmtWrapper

if TYPE_CHECKING:
    from couchbase.management.options import (DeployFunctionOptions,
                                              DropFunctionOptions,
                                              FunctionsStatusOptions,
                                              GetAllFunctionOptions,
                                              GetFunctionOptions,
                                              PauseFunctionOptions,
                                              ResumeFunctionOptions,
                                              UndeployFunctionOptions,
                                              UpsertFunctionOptions)


class EventingFunctionManager(EventingFunctionManagerLogic):
    def __init__(self, connection):
        super().__init__(connection)

    @EventingFunctionMgmtWrapper.block(None, EventingFunctionManagerLogic._ERROR_MAPPING)
    def upsert_function(
        self,
        function,  # type: EventingFunction
        *options,  # type: UpsertFunctionOptions
        **kwargs  # type: Dict[str, Any]
    ) -> None:
        super().upsert_function(function, *options, **kwargs)

    @EventingFunctionMgmtWrapper.block(None, EventingFunctionManagerLogic._ERROR_MAPPING)
    def drop_function(
        self,
        name,  # type: str
        *options,  # type: DropFunctionOptions
        **kwargs  # type: Any
    ) -> None:
        super().drop_function(name, *options, **kwargs)

    @EventingFunctionMgmtWrapper.block(None, EventingFunctionManagerLogic._ERROR_MAPPING)
    def deploy_function(
        self,
        name,  # type: str
        *options,  # type: DeployFunctionOptions
        **kwargs  # type: Any
    ) -> None:
        super().deploy_function(name, *options, **kwargs)

    @EventingFunctionMgmtWrapper.block(EventingFunction, EventingFunctionManagerLogic._ERROR_MAPPING)
    def get_all_functions(
        self,
        *options,  # type: GetAllFunctionOptions
        **kwargs  # type: Any
    ) -> List[EventingFunction]:
        return super().get_all_functions(*options, **kwargs)

    @EventingFunctionMgmtWrapper.block(EventingFunction, EventingFunctionManagerLogic._ERROR_MAPPING)
    def get_function(
        self,
        name,  # type: str
        *options,  # type: GetFunctionOptions
        **kwargs  # type: Any
    ) -> EventingFunction:
        return super().get_function(name, *options, **kwargs)

    @EventingFunctionMgmtWrapper.block(None, EventingFunctionManagerLogic._ERROR_MAPPING)
    def pause_function(
        self,
        name,  # type: str
        *options,  # type: PauseFunctionOptions
        **kwargs  # type: Any
    ) -> None:
        super().pause_function(name, *options, **kwargs)

    @EventingFunctionMgmtWrapper.block(None, EventingFunctionManagerLogic._ERROR_MAPPING)
    def resume_function(
        self,
        name,  # type: str
        *options,  # type: ResumeFunctionOptions
        **kwargs  # type: Any
    ) -> None:
        super().resume_function(name, *options, **kwargs)

    @EventingFunctionMgmtWrapper.block(None, EventingFunctionManagerLogic._ERROR_MAPPING)
    def undeploy_function(
        self,
        name,  # type: str
        *options,  # type: UndeployFunctionOptions
        **kwargs  # type: Any
    ) -> None:
        super().undeploy_function(name, *options, **kwargs)

    @EventingFunctionMgmtWrapper.block(EventingFunctionsStatus, EventingFunctionManagerLogic._ERROR_MAPPING)
    def functions_status(
        self,
        *options,  # type: FunctionsStatusOptions
        **kwargs  # type: Any
    ) -> EventingFunctionsStatus:
        return super().functions_status(*options, **kwargs)

    def _get_status(
        self,
        name,  # type: str
    ) -> EventingFunctionStatus:

        statuses = self.functions_status()

        if statuses.functions:
            return next((f for f in statuses.functions if f.name == name), None)

        return None
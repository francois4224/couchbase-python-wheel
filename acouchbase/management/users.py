from typing import (TYPE_CHECKING,
                    Any,
                    Awaitable,
                    Iterable)

from acouchbase.management.logic import UserMgmtWrapper
from couchbase.management.logic.users_logic import (Group,
                                                    RoleAndDescription,
                                                    User,
                                                    UserAndMetadata,
                                                    UserManagerLogic)

if TYPE_CHECKING:
    from couchbase.management.options import (DropGroupOptions,
                                              DropUserOptions,
                                              GetAllGroupsOptions,
                                              GetAllUsersOptions,
                                              GetGroupOptions,
                                              GetRolesOptions,
                                              GetUserOptions,
                                              UpsertGroupOptions,
                                              UpsertUserOptions)


class UserManager(UserManagerLogic):

    def __init__(self, connection, loop):
        super().__init__(connection)
        self._loop = loop

    @property
    def loop(self):
        """
        **INTERNAL**
        """
        return self._loop

    @UserMgmtWrapper.inject_callbacks(UserAndMetadata, UserManagerLogic._ERROR_MAPPING)
    def get_user(self,
                 username,  # type: str
                 *options,  # type: GetUserOptions
                 **kwargs   # type: Any
                 ) -> Awaitable[UserAndMetadata]:
        super().get_user(username, *options, **kwargs)

    @UserMgmtWrapper.inject_callbacks(UserAndMetadata, UserManagerLogic._ERROR_MAPPING)
    def get_all_users(self,
                      *options,  # type: GetAllUsersOptions
                      **kwargs  # type: Any
                      ) -> Awaitable[Iterable[UserAndMetadata]]:
        super().get_all_users(*options, **kwargs)

    @UserMgmtWrapper.inject_callbacks(None, UserManagerLogic._ERROR_MAPPING)
    def upsert_user(self,
                    user,     # type: User
                    *options,  # type: UpsertUserOptions
                    **kwargs  # type: Any
                    ) -> Awaitable[None]:

        super().upsert_user(user, *options, **kwargs)

    @UserMgmtWrapper.inject_callbacks(None, UserManagerLogic._ERROR_MAPPING)
    def drop_user(self,
                  username,  # type: str
                  *options,  # type: DropUserOptions
                  **kwargs   # type: Any
                  ) -> Awaitable[None]:
        super().drop_user(username, *options, **kwargs)

    @UserMgmtWrapper.inject_callbacks(RoleAndDescription, UserManagerLogic._ERROR_MAPPING)
    def get_roles(self,
                  *options,  # type: GetRolesOptions
                  **kwargs   # type: Any
                  ) -> Awaitable[Iterable[RoleAndDescription]]:
        super().get_roles(*options, **kwargs)

    @UserMgmtWrapper.inject_callbacks(Group, UserManagerLogic._ERROR_MAPPING)
    def get_group(self,
                  group_name,   # type: str
                  *options,     # type: GetGroupOptions
                  **kwargs      # type: Any
                  ) -> Awaitable[Group]:
        super().get_group(group_name, *options, **kwargs)

    @UserMgmtWrapper.inject_callbacks(Group, UserManagerLogic._ERROR_MAPPING)
    def get_all_groups(self,
                       *options,    # type: GetAllGroupsOptions
                       **kwargs     # type: Any
                       ) -> Awaitable[Iterable[Group]]:
        super().get_all_groups(*options, **kwargs)

    @UserMgmtWrapper.inject_callbacks(None, UserManagerLogic._ERROR_MAPPING)
    def upsert_group(self,
                     group,     # type: Group
                     *options,  # type: UpsertGroupOptions
                     **kwargs   # type: Any
                     ) -> Awaitable[None]:
        super().upsert_group(group, *options, **kwargs)

    @UserMgmtWrapper.inject_callbacks(None, UserManagerLogic._ERROR_MAPPING)
    def drop_group(self,
                   group_name,  # type: str
                   *options,    # type: DropGroupOptions
                   **kwargs     # type: Any
                   ) -> Awaitable[None]:
        super().drop_group(group_name, *options, **kwargs)
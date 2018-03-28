import unittest
import transaction
from pyramid import testing

from tracim.models.data import Workspace
from tracim.models.data import Content
from tracim.logger import logger
from tracim.fixtures import FixturesLoader
from tracim.fixtures.users_and_groups import Base as BaseFixture


class BaseTest(unittest.TestCase):
    """
    Pyramid default test.
    """
    def setUp(self):
        logger.debug(self, 'Setup Test...')
        self.config = testing.setUp(settings={
            'sqlalchemy.url': 'sqlite:///:memory:'
        })
        self.config.include('tracim.models')
        settings = self.config.get_settings()

        from tracim.models import (
            get_engine,
            get_session_factory,
            get_tm_session,
            )

        self.engine = get_engine(settings)
        session_factory = get_session_factory(self.engine)

        self.session = get_tm_session(session_factory, transaction.manager)
        self.init_database()

    def init_database(self):
        logger.debug(self, 'Init Database Schema...')
        from tracim.models.meta import DeclarativeBase
        DeclarativeBase.metadata.create_all(self.engine)

    def tearDown(self):
        logger.debug(self, 'TearDown Test...')
        from tracim.models.meta import DeclarativeBase

        testing.tearDown()
        transaction.abort()
        DeclarativeBase.metadata.drop_all(self.engine)

# class DefaultTest(object):
#
#     def _create_workspace_and_test(self, name, user) -> Workspace:
#         """
#         All extra parameters (*args, **kwargs) are for Workspace init
#         :return: Created workspace instance
#         """
#         WorkspaceApi(user).create_workspace(name, save_now=True)
#
#         eq_(1, self.session.query(Workspace).filter(Workspace.label == name).count())
#         return self.session.query(Workspace).filter(Workspace.label == name).one()
#
#     def _create_content_and_test(self, name, workspace, *args, **kwargs) -> Content:
#         """
#         All extra parameters (*args, **kwargs) are for Content init
#         :return: Created Content instance
#         """
#         content = Content(*args, **kwargs)
#         content.label = name
#         content.workspace = workspace
#         self.session.add(content)
#         self.session.flush()
#
#         eq_(1, ContentApi.get_canonical_query().filter(Content.label == name).count())
#         return ContentApi.get_canonical_query().filter(Content.label == name).one()
#
#
# class StandardTest(BaseTest):
#     """
#     BaseTest with default fixtures
#     """
#     fixtures = [BaseFixture]
#
#     def init_database(self):
#         BaseTest.init_database(self)
#         fixtures_loader = FixturesLoader([BaseFixture])
#         fixtures_loader.loads(self.fixtures)
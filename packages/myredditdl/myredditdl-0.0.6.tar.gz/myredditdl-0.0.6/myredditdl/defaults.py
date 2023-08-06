import pathlib
import os
import myredditdl.utils as utils
from myredditdl.config_handler import ConfigHandler


class Defaults:
    def __init__(self, debug=False) -> None:
        self.log = utils.setup_logger(__name__)
        self.config_handler = ConfigHandler()
        self.debug = debug

    @property
    def home_dir(self) -> str:
        return os.path.expanduser('~')

    @property
    def project_parent_dir(self) -> str:
        return str(pathlib.Path(__file__).parent.parent) + os.sep

    @property
    def src_dir(self) -> str:
        ''' Source files folder'''
        return str(pathlib.Path(__file__).parent) + os.sep

    @property
    def debug_media_dir(self) -> str:
        ''' Source files folder'''
        return str(pathlib.Path(__file__).parent) + \
            os.sep + 'debug_media' + os.sep

    @property
    def metadata_folder(self) -> str:
        return self.src_dir + 'metadata' + os.sep

    @property
    def debug_log_file(self) -> str:
        return self.src_dir + os.sep + 'debug.log'

    @property
    def debug_path(self) -> str:
        return str(self.project_parent_dir + 'debug_media' + os.sep)

    @property
    def metadata_suffix(self):
        return '_debug.json' if self.debug else '_metadata.json'

    @property
    def metadata_file(self) -> str:
        ''' Returns the full path of the metadata file'''
        username = self.config_handler.get_client_username()
        return self.metadata_folder + username + self.metadata_suffix

    @property
    def media_path(self):
        if self.debug:
            return self.debug_media_dir
        return self.config_handler.get_media_path()

    @property
    def current_prefix(self):
        return self.config_handler.get_prefix()

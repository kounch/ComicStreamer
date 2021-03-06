#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# -*- mode: Python; tab-width: 4; indent-tabs-mode: nil; -*-
# Do not change the previous lines. See PEP 8, PEP 263.
#
"""
foldername retrieval functions for comicstreamer app

Copyright 2014  Anthony Beville

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

import os
import sys
import platform
import logging

from comicstreamerlib.options import Options


class AppFolders():
    @staticmethod
    def makeFolders():
        def make(folder):
            if not os.path.exists(folder):
                os.makedirs(folder)

        make(AppFolders.logs())
        make(AppFolders.settings())
        make(AppFolders.appData())

    @staticmethod
    def runningAtRoolLevel():
        return False

    @staticmethod
    def windowsAppDataFolder():
        return os.environ['APPDATA']

    @staticmethod
    def userFolder():
        opts = Options()
        opts.parseCmdLineArgs()

        if opts.user_dir is not None:
            folder = opts.user_dir
        elif platform.system() == "Windows":
            folder = os.path.join(AppFolders.windowsAppDataFolder(),
                                  'ComicStreamer')
        elif platform.system() == "Darwin":
            folder = os.path.join(
                os.path.expanduser('~'),
                'Library/Application Support/ComicStreamer')
        else:
            folder = os.path.join(os.path.expanduser('~'), '.ComicStreamer')

        return folder

    @staticmethod
    def appBase():
        if getattr(sys, 'frozen', None):
            if platform.system() == "Darwin":
                return sys._MEIPASS
            else:  # Windows
                return os.path.dirname(os.path.abspath(str(sys.executable)))
        else:
            return os.path.dirname(os.path.abspath(str(__file__)))

    @staticmethod
    def logs():
        if AppFolders.runningAtRoolLevel():
            if platform.system() == "Windows":
                folder = os.path.join(AppFolders.windowsAppDataFolder(),
                                      'ComicStreamer')
            else:
                folder = "/var/log/ComicStreamer"
        else:
            folder = os.path.join(AppFolders.userFolder(), "logs")
        return folder

    @staticmethod
    def settings():
        if AppFolders.runningAtRoolLevel():
            if platform.system() == "Windows":
                folder = os.path.join(AppFolders.windowsAppDataFolder(),
                                      'ComicStreamer')
            elif platform.system() == "Darwin":
                folder = os.path.join(
                    '/Library/Application Support/ComicStreamer')
            else:
                folder = "/etc/ComicStreamer"
        else:
            folder = os.path.join(AppFolders.userFolder())
        return folder

    @staticmethod
    def appData():
        if AppFolders.runningAtRoolLevel():
            if platform.system() == "Windows":
                folder = os.path.join(AppFolders.windowsAppDataFolder(),
                                      'ComicStreamer')
            elif platform.system() == "Darwin":
                folder = os.path.join(
                    '/Library/Application Support/ComicStreamer')
            else:
                folder = "/var/lib/ComicStreamer"
        else:
            folder = os.path.join(AppFolders.userFolder())
        return folder

    @staticmethod
    def imagePath(filename):
        return os.path.join(AppFolders.appBase(), "static", "images", filename)

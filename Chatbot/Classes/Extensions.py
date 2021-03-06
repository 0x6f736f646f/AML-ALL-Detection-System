############################################################################################
#
# The MIT License (MIT)
# 
# Acute Myeloid Leukemia Detection System 
# Copyright (C) 2018 Adam Milton-Barker (AdamMiltonBarker.com)
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
#
# Title:         Acute Myeloid Leukemia Detection System Extensions Tools
# Description:   Extensions functions for the Acute Myeloid Leukemia Detection System.
# Configuration: required/confs.json
# Last Modified: 2018-12-22
#
############################################################################################

class Extensions():

    def __init__(self):
        pass

    def setExtension(self, intent):

        ###############################################################
        #
        # Sets and returns the extension path and responses
        #
        ###############################################################

        extensionResponses = []
        extension = None
        entities  = False

        extension = intent["extension"]["function"] if intent["extension"]["function"] !="" else None

        if extension != None:
            extensionResponses = intent["extension"]["responses"]
            entities = intent["extension"]["entities"]

        return extension, extensionResponses, entities
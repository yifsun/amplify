#! /usr/bin/env python
# Quex is  free software;  you can  redistribute it and/or  modify it  under the
# terms  of the  GNU Lesser  General  Public License  as published  by the  Free
# Software Foundation;  either version 2.1 of  the License, or  (at your option)
# any later version.
# 
# This software is  distributed in the hope that it will  be useful, but WITHOUT
# ANY WARRANTY; without even the  implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE.  See the  GNU Lesser General Public License for more
# details.
# 
# You should have received a copy of the GNU Lesser General Public License along
# with this  library; if not,  write to the  Free Software Foundation,  Inc., 59
# Temple Place, Suite 330, Boston, MA 02111-1307 USA
#
# (C) Frank-Rene Schaefer
#_______________________________________________________________________________
# IMPORTANT: This file shall be import-able by any 'normal' module of Quex.    #
#            For this, it was a designated design goal to make sure that the   #
#            imports are 'flat' and only cause environment or outer modules.   #
#_______________________________________________________________________________
from quex.engine.misc.enum           import Enum
from quex.engine.generator.code.base import CodeFragment_NULL
from quex.input.setup                import QuexSetup, SETUP_INFO

#------------------------------------------------------------------------------
# setup: All information of the user's desired setup.
#------------------------------------------------------------------------------
setup = QuexSetup(SETUP_INFO)

class Lng_class:
    """Provide shortcut to 'Setup.language_db'.
    ___________________________________________________________________________
    During code generation, there is an excessive reference to the language
    database, i.e. the instance which tells who to do things in the output
    language. Instead of writing 'Setup.language_db.xyz()' it shall be possible
    to write 'Lng.xyz()' which helps to keep the code clean. 

    The global object 'Lng' is an instance of this class. It references to 
    'Setup.language_db', even if the setting of '.language_db' changes.
    ___________________________________________________________________________
    """
    def __init__(self, TheSetup):
        self.__setup = TheSetup
    def __getattr__(self, Attr): 
        language_db = self.__setup.language_db
        try:             return getattr(language_db, Attr)
        except KeyError: raise AttributeError

Lng = Lng_class(setup)

#------------------------------------------------------------------------------
# StateIndices: Values to be used as target states for transitions
#------------------------------------------------------------------------------
E_StateIndices = Enum("DROP_OUT", 
                      "RELOAD_FORWARD",
                      "RELOAD_BACKWARD",
                      "END_OF_PRE_CONTEXT_CHECK",
                      "RECURSIVE",
                      "ALL", 
                      "ANALYZER_REENTRY", 
                      "NONE", 
                      "VOID") 

E_PreContextIDs  = Enum("NONE",    
                        "BEGIN_OF_LINE", 
                        "_DEBUG_NAME_PreContextIDs")

E_PostContextIDs = Enum("NONE", 
                        "IRRELEVANT",
                        "_DEBUG_NAME_E_PostContextIDs")

E_TransitionN = Enum("VOID", 
                     "LEXEME_START_PLUS_ONE",
                     "IRRELEVANT",
                     "_DEBUG_NAME_TransitionNs")

E_TriggerIDs = Enum("NONE", 
                    "_DEBUG_NAME_TriggerIDs")

E_InputActions = Enum("DEREF", 
                      "INCREMENT", 
                      "INCREMENT_THEN_DEREF", 
                      "DECREMENT",
                      "DECREMENT_THEN_DEREF",
                      "_DEBUG_InputActions")

E_Compression = Enum("PATH", 
                     "PATH_UNIFORM",
                     "TEMPLATE",
                     "TEMPLATE_UNIFORM",
                     "_DEBUG_Compression")

E_Count = Enum("VIRGIN", 
               "VOID",
               "NONE",
               "_DEBUG_Count")

E_CharacterCountType = Enum("COLUMN", 
                            "LINE", 
                            "GRID", 
                            "BEGIN_NEWLINE_SUPPRESSOR",
                            "BEGIN_NEWLINE",
                            "BEGIN_COMMENT_TO_NEWLINE",
                            "END_NEWLINE",
                            "BAD", 
                            "WHITESPACE", 
                            "_DEBUG_CharacterCountType")

E_Commonality = Enum("NONE", "BOTH", "A_IN_B", "B_IN_A")

E_TerminalType = Enum("MATCH_PATTERN",   # A pattern match
                      "MATCH_FAILURE",   # Nothing has matched
                      "SKIP_RANGE_OPEN", # Nothing has matched
                      "END_OF_STREAM",   # End of stream has been reached
                      "PLAIN",           # Plain code (likely generated by Quex)
                      "_DEBUG_TerminalType")

E_IncidenceIDs = Enum(
# Incidences encompass 'pattern acceptance events' and any other incidences
# mentioned below. IncidenceID-s are keys to the standard_incidence_db.
    "AFTER_MATCH",
    "BIPD_TERMINATED",
    "CODEC_ERROR",
    "DEDENT",
    "END_OF_STREAM",
    "EXIT_LOOP",
    "GOOD_TRANSITION",
    "INDENTATION_BAD",
    "INDENTATION_ERROR",
    "INDENTATION_HANDLER",
    "INDENTATION_INDENT",
    "INDENTATION_NEWLINE", 
    "INDENTATION_NODENT",
    "INDENTATION_DEDENT",
    "INDENTATION_N_DEDENT",
    "MATCH",
    "MATCH_FAILURE",
    "MODE_ENTRY",
    "MODE_EXIT",
    "PRE_CONTEXT_FULFILLED",
    "SKIP", 
    "SKIP_NESTED_RANGE", 
    "SKIP_RANGE", 
    "SKIP_RANGE_OPEN",
    "VOID",
    "_DEBUG_Events")

E_IncidenceIDs_SubsetAcceptanceIDs = [
    E_IncidenceIDs.MATCH_FAILURE,
    E_IncidenceIDs.PRE_CONTEXT_FULFILLED, 
    E_IncidenceIDs.BIPD_TERMINATED, 
    E_IncidenceIDs.VOID,
    E_IncidenceIDs.INDENTATION_HANDLER,
]

E_IncidenceIDs_Subset_Special = [
    E_IncidenceIDs.INDENTATION_HANDLER,
    E_IncidenceIDs.SKIP, 
    E_IncidenceIDs.SKIP_NESTED_RANGE, 
    E_IncidenceIDs.SKIP_RANGE, 
    E_IncidenceIDs.SKIP_RANGE_OPEN,
]

E_MapImplementationType = Enum("STATE_MACHINE_TRIVIAL", 
                               "STATE_MACHINE",
                               "PLAIN_MAP", 
                               "_DEBUG_MapImplementationType")

E_Border = Enum("BEGIN", "END", "UNDEFINED", "_DEBUG_Border")

E_DoorIdIndex = Enum("DROP_OUT", 
                     "TRANSITION_BLOCK", 
                     "ACCEPTANCE", 
                     "BIPD_RETURN", 
                     "STATE_MACHINE_ENTRY", 
                     "EMPTY", 
                     "GLOBAL_STATE_ROUTER", 
                     "GLOBAL_END_OF_PRE_CONTEXT_CHECK", 
                     "GLOBAL_REENTRY",
                     "RETURN_WITH_ON_AFTER_MATCH",
                     "CONTINUE_WITH_ON_AFTER_MATCH",
                     "CONTINUE_WITHOUT_ON_AFTER_MATCH",
                     "_DEBUG_DoorIdIndex") 

E_Cmd = Enum("Accepter",
             "Assign",
             "AssignConstant",
             "ColumnCountAdd",
             "ColumnCountGridAdd",
             "ColumnCountReferencePDeltaAdd",
             "ColumnCountReferencePSet",
             "GotoDoorId",
             "GotoDoorIdIfInputPNotEqualPointer",
             "IfPreContextSetPositionAndGoto",
             "IndentationHandlerCall",
             "InputPDecrement",
             "InputPDereference",
             "InputPIncrement",
             "LexemeResetTerminatingZero",
             "LineCountAdd",
             "PathIteratorSet",
             "PreContextOK",
             "PrepareAfterReload",
             "Router",
             "RouterOnStateKey",
             "QuexDebug",
             "QuexAssertNoPassage",
             "StoreInputPosition",
             "TemplateStateKeySet",
             "_DEBUG_Commands")


#-----------------------------------------------------------------------------------------
# standard_incidence_db: Stores names of event handler functions as keys and their meaning
#                        as their associated values.
#-----------------------------------------------------------------------------------------
standard_incidence_db = {
    "on_entry":                  (E_IncidenceIDs.MODE_ENTRY,          "On entry of a mode."),
    "on_exit":                   (E_IncidenceIDs.MODE_EXIT,           "On exit of a mode."),
    "on_indent":                 (E_IncidenceIDs.INDENTATION_INDENT,  "On opening indentation."),
    "on_nodent":                 (E_IncidenceIDs.INDENTATION_NODENT,  "On same indentation."),
    "on_dedent":                 (E_IncidenceIDs.INDENTATION_DEDENT,  "On closing indentation'."),
    "on_n_dedent":               (E_IncidenceIDs.INDENTATION_N_DEDENT, "On closing indentation'."),
    "on_indentation_error":      (E_IncidenceIDs.INDENTATION_ERROR,   "Closing indentation on non-border."),
    "on_indentation_bad":        (E_IncidenceIDs.INDENTATION_BAD,     "On bad character in indentation."),
    "on_indentation":            (E_IncidenceIDs.INDENTATION_HANDLER, "General Indentation Handler."),
    "on_match":                  (E_IncidenceIDs.MATCH,       "On each match (before pattern action)."),
#   TODO        "on_token_stamp":            "On event of token stamping.",
#   instead of: QUEX_ACTION_TOKEN_STAMP 
    "on_after_match":            (E_IncidenceIDs.AFTER_MATCH,         "On each match (after pattern action)."),
    "on_failure":                (E_IncidenceIDs.MATCH_FAILURE,       "In case that no pattern matches."),
    "on_skip_range_open":        (E_IncidenceIDs.SKIP_RANGE_OPEN,     "On missing skip range delimiter."),
    "on_end_of_stream":          (E_IncidenceIDs.END_OF_STREAM,       "On end of file/stream."),
}

#-----------------------------------------------------------------------------------------
# mode_description_db: storing the mode information into a dictionary:
#            key  = mode name
#            item = ModeDescription object
#
# ModeDescription-s are the direct product of parsing. They are later translated into
# Mode-s.
#-----------------------------------------------------------------------------------------
mode_description_db = {}
#-----------------------------------------------------------------------------------------
# mode_db: storing the mode information into a dictionary:
#            key  = mode name
#            item = Mode object
#
# A Mode is a more 'fermented' container of information about a mode. It is based on
# a ModeDescription.
#-----------------------------------------------------------------------------------------
mode_db = {}

#-----------------------------------------------------------------------------------------
# initial_mode: mode in which the lexcial analyser shall start
#-----------------------------------------------------------------------------------------
initial_mode = CodeFragment_NULL

#-----------------------------------------------------------------------------------------
# header: code fragment that is to be pasted before mode transitions
#         and pattern action pairs (e.g. '#include<something>'
#-----------------------------------------------------------------------------------------
header = CodeFragment_NULL

#-----------------------------------------------------------------------------------------
# class_body_extension: code fragment that is to be pasted inside the class definition
#                       of the lexical analyser class.
#-----------------------------------------------------------------------------------------
class_body_extension = CodeFragment_NULL

#-----------------------------------------------------------------------------------------
# class_constructor_extension: code fragment that is to be pasted inside the lexer class constructor
#-----------------------------------------------------------------------------------------
class_constructor_extension = CodeFragment_NULL

#-----------------------------------------------------------------------------------------
# memento_extension: fragment to be pasted into the memento  class's body.
#-----------------------------------------------------------------------------------------
memento_class_extension = CodeFragment_NULL
#-----------------------------------------------------------------------------------------
# memento_pack_extension: fragment to be pasted into the function that packs the
#                         lexical analyzer state in a memento.
#-----------------------------------------------------------------------------------------
memento_pack_extension = CodeFragment_NULL
#-----------------------------------------------------------------------------------------
# memento_unpack_extension: fragment to be pasted into the function that unpacks the
#                           lexical analyzer state in a memento.
#-----------------------------------------------------------------------------------------
memento_unpack_extension = CodeFragment_NULL

fragment_db = {
    "header":         "header",
    "body":           "class_body_extension",
    "init":           "class_constructor_extension",
    "memento":        "memento_class_extension",
    "memento_pack":   "memento_pack_extension",
    "memento_unpack": "memento_unpack_extension",
}

all_section_title_list = ["start", "define", "token", "mode", "repeated_token", "token_type" ] + fragment_db.keys()

#-----------------------------------------------------------------------------------------
# shorthand_db: user defined names for regular expressions.
#-----------------------------------------------------------------------------------------
shorthand_db = {}

#-----------------------------------------------------------------------------------------
# signal_character_list: List of characters which carry a specific meaning and shall
#                        not appear in the input stream.
#-----------------------------------------------------------------------------------------
def signal_character_list(TheSetup):
    return [
        (TheSetup.buffer_limit_code, "Buffer Limit Code"),
        (TheSetup.path_limit_code,   "Path Limit Code")
    ]

#-----------------------------------------------------------------------------------------
# token_id_db: list of all defined token-ids together with the file position
#              where they are defined. See token_ide_maker, class TokenInfo.
#-----------------------------------------------------------------------------------------
token_id_db = {}
def get_used_token_id_set():
    return [ token.number for token in token_id_db.itervalues() if token.number is not None ]

#-----------------------------------------------------------------------------------------
# token_id_foreign_set: Set of token ids which came from an external token id file.
#                       All tokens which are not defined in an external token id file
#                       are defined by quex.
#-----------------------------------------------------------------------------------------
token_id_foreign_set = set()

#-----------------------------------------------------------------------------------------
# token_id_implicit_list: Keep track of all token identifiers that ware defined 
#                         implicitly, i.e. not in a token section or in a token id file. 
#                         Each list element has three cells:
#                         [ Prefix-less Token ID, Line number in File, File Name]
#-----------------------------------------------------------------------------------------
token_id_implicit_list = []

#-----------------------------------------------------------------------------------------
# token_repetition_support: Quex can be told to return multiple times the same
#                           token before further analyzsis happens. For this,
#                           the engine needs to know how to read and write the
#                           repetition number in the token itself.
# If the 'token_repetition_token_id_list' is None, then the token repetition feature
# is disabled. Otherwise, token repetition in 'token-receiving.i' is enabled
# and the token id that can be repeated is 'token_repetition_token_id'.
#-----------------------------------------------------------------------------------------
token_repetition_token_id_list = ""

#-----------------------------------------------------------------------------------------
# token_type_definition: Object that defines a (user defined) token class.
#
# The first token_type section defines the variable as a real 'TokenTypeDescriptor'.
#
# The setup_parser.py checks for the specification of a manually written token class file. 
# If so then an object of type 'ManualTokenClassSetup' is assigned.
#
# Default = None is detected by the 'input/file/core.py' and triggers the parsing of the 
# default token type description. 
#          
#-----------------------------------------------------------------------------------------
token_type_definition = None

#-----------------------------------------------------------------------------------------
# Helper functions about required features.
#-----------------------------------------------------------------------------------------
# Determine whether the lexical analyser needs indentation counting
# support. if one mode has an indentation handler, than indentation
# support must be provided.                                         
__required_support_indentation_count = False
def required_support_indentation_count_set():
    global __required_support_indentation_count
    __required_support_indentation_count = True
def required_support_indentation_count():
    global __required_support_indentation_count
    return __required_support_indentation_count

# If one single pattern in one mode depends on begin of line, then
# the begin of line condition must be supported. Otherwise not.
# The requirement can be only set, but no unset!
__required_support_begin_of_line = False
def required_support_begin_of_line_set():
    global __required_support_begin_of_line
    __required_support_begin_of_line = True
def required_support_begin_of_line():
    global __required_support_begin_of_line
    return __required_support_begin_of_line

def deprecated(*Args):
    """This function is solely to be used as setter/getter property, 
       of member variables that are deprecated. This way misuse
       can be detected. Example usage:

       class X(object):  # Class must be derived from 'object'
           ...
           my_old = property(deprecated, deprecated, "Alarm on 'my_old'")
    """
    assert False

class DefaultCounterFunctionDB:
    """Default counters may be used in several modes. This database
    keeps track of implementations. If an implementation is done for
    one mode, another mode may refer it it.
    """
    __db = []
    @staticmethod
    def get_function_name(CCFactory):
        """Returns name of function which already implemented the 'CounterDb'.
        Otherwise, it returns 'None' if no such function exists.
        """
        for factory, function_name in DefaultCounterFunctionDB.__db:
            if factory.is_equal(CCFactory): 
                return function_name
        return None

    @staticmethod
    def function_name_iterable():
        for counter_db, function_name in DefaultCounterFunctionDB.__db:
            yield function_name


    @staticmethod
    def enter(CCFactory, FunctionName):
        for function_name in DefaultCounterFunctionDB.function_name_iterable():
            assert function_name != FunctionName
        DefaultCounterFunctionDB.__db.append((CCFactory, FunctionName))

    @staticmethod
    def clear():
        del DefaultCounterFunctionDB.__db[:]
 


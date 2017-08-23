from ipykernel.kernelbase import Kernel

class KernelName(Kernel):
    implementation = 'Pig Latin'
    # Version of the kernel
    implementation_version = '1.0'
    # The name of hte language implemented
    language = 'no-op'
    # Version of the language implemented
    language_version = '1.0'
    # Banner displayed in console when using kernel 
    banner='A kernel to send back messages in Pig Latin'
    """
    - language_info stored in .ipynb JSON
    - mime_type should be one of the MIME types defined by CodeMirror.
        - http://codemirror.net/mode/index.html
    """
    language_info = {
        'name': 'Arbitrary',
        'mimetype': 'text/plain',
        'file_extension': '.txt',
    }

    def do_execute(self, code, silent, store_history=True, user_expressions=None,
                   allow_stdin=False):
        """
        Fulfill an execute request.

        Arguments
            code: The piece of code that needs to be executed
            silent: Whether or not to broadcast output or return an execute_result
        Keyword Arguments
            store_history: Whether or not to store this command in history
            user_expressions:
            allow_stdin:
        Return
            {
                'status': 'ok',
                'execution_count': self.execution_count,
                'payload': [],
                'user_expressions': {},
            }
        """
        pass

    def do_is_complete(self, code):
        """
        Fulfill an is_complete reuqest.

        Arguments:
            code: The piece of code that needs to be assessed

        Return:
            Whether or not `code` is a complete statement
        """
        pass

    def do_shutdown(self, restart):
        """
        Fulfill a do_complete request.

        Arguments:
            restart: Whether or not to start the kernel after shutdown
        """
        pass

    def do_history(self, hist_access_type, output, raw, session=None,
            start=None, stop=None, n=None, pattern=None, unique=False):
        """
        Fulfill a history request.

        Arguments
            hist_access_type: Whether to search in a "range" at the "tail" or
            "search" for a match
            output: Whether or not to return the output history
            raw: Whether or not to return the raw or transformed input history
        Keyword Arguments
            session:  If hist_access_type is "range" define the session to
            search in, the session counter is incremented every time the kernel
            is restarted
            start: If hist_access_type is "range" define the cell to start
            searching for history in
            stop: If hist_access_type is "range" define the cell to stop searching
            for history in
            n: If hist_access_type is "tail" or "search" get the last n cells
            pattern: If hist_access_type is "search" get the cells matching this
            pattern
            unique: Whether or not to include duplicated history items if
            hist_access_type is "search"
        Return
            {
                "content": (session, line_number, input) or
                (session, line_number, (input, output))
        """
        pass

    def do_inspect(self, code, cursor_pos, detail_level=0):
        """
        Fulfill an inspect request.

        Arguments
            code: The code snippet to get the inspection text for
            cursor_pos: The cursor position to get the inspection at
        Keyword Arguments
            detail_level:The level of detail to show in the inspection, can be 0
            or 1, the kernel should handle what to do based on this value
        Return
            {
                "status": "ok"
                "found": Whether or not the inspected object was found
                "data": The data result of the introspection
                "metadata": The metadata result of the introspection
        """
        pass

    def do_complete(self, code, cursor_pos):
        """
        Fulfill a complete request.

        Arguments
            code: The code snippet to get a completion for
            cursor_pos: The cursor position to get the completion at
        Return
            {
                "matches": The list of matches for the completion string
                "cursor_start": The start of the range that should be replaced if the completion is used
                "cursor_end": The end of the range that should be replaced if the completion is used
                "metadata: Additional information about the completion that can be used by the front end
                "status": "ok"
            }
        """
        pass

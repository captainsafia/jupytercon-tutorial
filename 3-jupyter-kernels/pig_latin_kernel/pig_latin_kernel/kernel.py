from ipykernel.kernelbase import Kernel

class PigLatinKernel(Kernel):
    implementation = 'Pig Latin'
    implementation_version = '1.0'
    language = 'no-op'
    language_version = '1.0'
    banner='A kernel to send back messages in Pig Latin'
    language_info = {
        'name': 'Arbitrary',
        'mimetype': 'text/plain',
        'file_extension': '.txt',
    }

    def convert_word_to_pig_latin(self, word):
        suffix = 'ay'
        first = word[0]
        if first in 'aeiou':
            return word
        else:
            return word[1:] + first + suffix

    def convert_to_pig_latin(self, content):
        words = content.lower().split(' ')
        converted = map(self.convert_word_to_pig_latin, words)
        return ' '.join(converted)

    def do_execute(self, code, silent, store_history=True, user_expressions=None,
                   allow_stdin=False):
        if not silent:
            pig_latined = self.convert_to_pig_latin(code)
            stream_content = {'name': 'stdout', 'text': pig_latined}
            self.send_response(self.iopub_socket, 'stream', stream_content)

        return {
            'status': 'ok',
            'execution_count': self.execution_count,
            'payload': [],
            'user_expressions': {},
       }

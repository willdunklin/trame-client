from trame.app import get_server

server = get_server()
server.client_type = "vue3"
state, ctrl = server.state, server.controller

state.count = 2
state.double = 4
state.client_type = server.client_type


@state.change("count")
def update_count(count, **kwargs):
    state.double = 2 * int(count)


state.trame__template_main = """
    <div>
        <label>{{ client_type }}</label>
        <div>count = {{ count }}</div>
        <div>2 x count = {{ double }}</div>
        <input type="range" min="0" max="10" step="1" v-model.number="count.value" />
        <input type="range" min="0" max="10" step="1" v-model.number="state.count" />
    </div>
"""

server.start()


import time
import sys
import os
import json
from flask import Flask, render_template, request, jsonify, url_for, redirect

from chatbotQuery.io import generate_info_reports
from chatbotQuery.io.prepare_reports import generate_html_states_table,\
    generate_html_transitions_table
from chatbotQuery.ui import HandlerConvesationUI


## Auxiliar functions
def filter_message(messageDict):
    filtered_fields = ["answer_status", "collection", "from", "posting_status",
                       "sending_status", "message"]
    answer = {}
    for field in filtered_fields:
        if field == "message":
            if isinstance(messageDict['message'], list):
                new_message = []
                for m in messageDict['message']:
                    if m['from'] == 'bot':
                        new_message.append(filter_message(m))
                answer['message'] = new_message
            else:
                answer['message'] = messageDict['message']
        else:
            if field in messageDict:
                answer[field] = messageDict[field]
    return answer


def jsonify_message(messageDict):
    ## Prepare text to show
    if messageDict['collection']:
        speechResponse = []
        for m in messageDict['message']:
            if m['from'] == 'bot':
                speechResponse.append(str(m['message']))
        speechResponse = str('\n'.join(speechResponse))
    else:
        speechResponse = str(messageDict['message'])
    ## Filter and adapt message
    answer = filter_message(messageDict)
    answer['speechResponse'] = speechResponse
    answer['status'] = 'OK'
    return answer


## App instantiation
db_conf_file = '/home/antonio/code/chatbot_query/examples/example_dbparser/db_handler_parameters.yml'
conv_conf_file = '/home/antonio/code/chatbot_query/examples/example_dbparser/dbparser_parameter.yml'
# Parser parameters
bot = HandlerConvesationUI.from_configuration_files(db_conf_file,
                                                    conv_conf_file)
app = Flask(__name__)


## States route
@app.route("/conversation_test")
def conversation_test():
    return render_template("testing_chat.html")


# Request Handler
@app.route('/conversation_test/api/v1', methods=['POST'])
def conversation_test_api():
    requestJson = request.get_json(silent=True)
    message = str(requestJson['input'])
    # Get message
    if (message == "quit") or (message is None):
        time.sleep(60)
        exit()

    if message is not None:
        # Get and format answer
        answer = bot.get_message({'message': message})
        if (answer is None):
            time.sleep(60)
            exit()

        # Send answer
        response_obj = jsonify(jsonify_message(answer))
        return response_obj


@app.route("/reset_conversation_test")
def reset_conversation():
    global bot
    bot = HandlerConvesationUI.from_configuration_files(db_conf_file,
                                                        conv_conf_file)
    return redirect(url_for('conversation_test'))


@app.route("/states_table")
def states_table_view():
    table, _, _, _, _, _ = generate_info_reports(conv_conf_file)
    table = generate_html_states_table(table)
    return render_template("table.html", name_title="States Table",
                           table=table)


@app.route("/transitions_table")
def transition_table_view():
    _, table, _, _, _, _ = generate_info_reports(conv_conf_file)
    table = generate_html_transitions_table(table)
    return render_template("table.html", name_title="Transitions table list",
                           table=table)


## Conversation Tree Graph
@app.route("/conversation_tree_graph")
def tree_graph_view():
    return render_template("tree_graph.html")


@app.route("/conversation_tree_graph/tree_graph.json")
def tree_graph_json():
    _, _, tree, _, _, _ = generate_info_reports(conv_conf_file)
    return jsonify(tree)


## Conversation Complete Graph
@app.route("/conversation_complete_graph")
def conversation_complete_graph_view():
    return render_template("complete_graph.html")


@app.route("/conversation_complete_graph/complete_graph.json")
def conversation_complete_graph_json():
    _, _, _, cg, _, _ = generate_info_reports(conv_conf_file)
    return jsonify(cg)


## Conversation Complete Graph
@app.route("/conversation_statemachine_graphs")
def conversation_graphs_view():
    _, _, _, _, graphs, _ = generate_info_reports(conv_conf_file)
    graphs = sorted(graphs, key=lambda x: (len(x[1].split('.')), x[0]))
    defaultmachine = graphs[0][1]
    statemachines = [g[1] for g in graphs[1:]]
    return render_template("statemachine_graphs.html",
                           defaultmachine=defaultmachine,
                           statemachines=statemachines)


@app.route("/conversation_statemachine_graphs/<query_sm>.json")
def conversation_graphs_json(query_sm=None):
    _, _, _, _, graphs, graphs_json = generate_info_reports(conv_conf_file)
    if query_sm is None:
        graphs = sorted(graphs, key=lambda x: (len(x[1].split('.')), x[0]))
        query_sm = graphs[0][1]
    if query_sm == 'graphs':
        filtered_graph = []
        for g in graphs_json:
            f_graph = {}
            f_graph['name'] = g['name']
            f_graph['nodes'] = g['nodes']
            f_graph['links'] = g['links']
            filtered_graph.append(f_graph)
    else:
        graph = list(filter(lambda x: x['name'] == query_sm, graphs_json))[0]
        filtered_graph = {}
        filtered_graph['nodes'] = graph['nodes']
        filtered_graph['links'] = graph['links']
    return jsonify(filtered_graph)


@app.route("/catalan_parliament")
def catalan_parliment_view():
    return render_template("catalan_parliament.html")


@app.route("/catalan_parliament/catalan_parliament.json")
def catalan_parliment_data():
    data = {}
    data['parliament'] = {'name': 'Parlament de Catalunya', 'seats': '135'}
    data['parties'] = [
        {"name": "Junts pel Sí", "code": "JxSi", "color": "#34cbcb"},
        {"name": "Ciutadans", "code": "C's", "color": "#ff8000"},
        {"name": "Partit Socialista de Catalunya", "code": "PSC",
         "color": "#e60000"},
        {"name": "Catalunya Sí Que es Pot", "code": "CSQP",
         "color": "#e60073"},
        {"name": "Partit Popular de Catalunya", "code": "PPC",
         "color": "#3333ff"},
        {"name": "Candidatures d'Unitat Popular", "code": "CUP",
         "color": "#ffff00"},
    ]
    data['results'] = {
        "Seats": {
            "JxSi": 62,
            "C's": 25,
            "PSC": 16,
            "CSQP": 11,
            "PPC": 11,
            "CUP": 10
        },
        "Proportional": {
            "JxSi":  0.45926,
            "C's": 0.185185,
            "PSC": 0.11852,
            "CSQP": 0.0814815,
            "PPC": 0.0814815,
            "CUP": 0.074074
        },
        "Shapley": {
            "JxSi":  2/3.,
            "C's": 1/15.,
            "PSC": 1/15.,
            "CSQP": 1/15.,
            "PPC": 1/15.,
            "CUP": 1/15.
        },
        "Banzhaf": {
            "JxSi":  0.75,
            "C's": 0.05,
            "PSC": 0.05,
            "CSQP": 0.05,
            "PPC": 0.05,
            "CUP": 0.05
        },
        "Winnable-Auto-Ideologia": {
            "JxSi": .322,
            "C's": .138,
            "PSC": .153,
            "CSQP": .147,
            "PPC": .113,
            "CUP": .127
        },
        "Worsable-Auto-Ideologia": {
            "JxSi": .368,
            "C's": .128,
            "PSC": .155,
            "CSQP": .144,
            "PPC": .093,
            "CUP": .111
        },
        "Winnable-Ideologia": {
            "JxSi": .363,
            "C's": .122,
            "PSC": .165,
            "CSQP": .150,
            "PPC": .095,
            "CUP": .103
        },
        "Worsable-Ideologia": {
            "JxSi": .412,
            "C's": .109,
            "PSC": .170,
            "CSQP": .146,
            "PPC": .077,
            "CUP": .085
        },
        "Winnable-Auto-Nacionalismo": {
            "JxSi": .351,
            "C's": .124,
            "PSC": .130,
            "CSQP": .145,
            "PPC": .106,
            "CUP": .144
        },
        "Worsable-Auto-Nacionalismo": {
            "JxSi": .362,
            "C's": .117,
            "PSC": .126,
            "CSQP": .150,
            "PPC": .092,
            "CUP": .153
        },
        "Winnable-Nacionalismo": {
            "JxSi": .383,
            "C's": .095,
            "PSC": .135,
            "CSQP": .165,
            "PPC": .070,
            "CUP": .150
        },
        "Worsable-Nacionalismo": {
            "JxSi": .408,
            "C's": .082,
            "PSC": .129,
            "CSQP": .173,
            "PPC": .057,
            "CUP": .151
        },
        "Winnable-Independentismo": {
            "JxSi": .438,
            "C's": .073,
            "PSC": .094,
            "CSQP": .102,
            "PPC": .077,
            "CUP": .214
        },
        "Worsable-Independentismo": {
            "JxSi": .431,
            "C's": .067,
            "PSC": .091,
            "CSQP": .101,
            "PPC": .071,
            "CUP": .240
        }
    }
    return jsonify(data)


@app.route("/spanish_parliament")
def spanish_parliment_view():
    return render_template("spanish_parliament.html")


@app.route("/spanish_parliament/spanish_parliament.json")
def spanish_parliment_data():
    data = {}
    data['parliament'] = {'name': 'Congreso de los Diputados', 'seats': '350'}
    data['parties'] = [
        {"name": "Partido Popular", "code": "PP", "color": "#3333ff"},
        {"name": "Partido Socialista Obrero Español", "code": "PSOE",
         "color": "#e60000"},
        {"name": "Podemos", "code": "Podemos", "color": "#660033"},
        {"name": "Ciutadans", "code": "C's", "color": "#ff8000"},
        {"name": "Esquerra Republicana de Catalunya", "code": "ERC", "color": "#ffd11a"},
        {"name": "Democràcia i Llibertat", "code": "DiL", "color": "#000066"},
        {"name": "Partido Nacionalista Vasco", "code": "PNV", "color": "#009933"},
        {"name": "Izquierda Unida", "code": "IU", "color": "#660000"},
        {"name": "EH Bildu", "code": "Bildu", "color": "#99ff33"},
        {"name": "Coalicion Canarias", "code": "CC", "color": "#e6e600"},
    ]
    data['results'] = {
        "Seats": {
            "PP": 123,
            "PSOE": 90,
            "Podemos": 69,
            "C's": 40,
            "ERC": 9,
            "DiL": 8,
            "PNV": 6,
            "IU": 2,
            "Bildu": 2,
            "CC": 1
        },
        "Proportional": {
            "PP": .351,
            "PSOE": .257,
            "Podemos": .197,
            "C's": .114,
            "ERC": .026,
            "DiL": .023,
            "PNV": .017,
            "IU": .006,
            "Bildu": .006,
            "CC": .003
        },
        "Shapley": {
            "PP": .402,
            "PSOE": .220,
            "Podemos": .220,
            "C's": .070,
            "ERC": .030,
            "DiL": .025,
            "PNV": .020,
            "IU": .006,
            "Bildu": .006,
            "CC": .002
        },
        "Banzhaf": {
            "PP": .378,
            "PSOE": .210,
            "Podemos": .210,
            "C's": .084,
            "ERC": .040,
            "DiL": .033,
            "PNV": .026,
            "IU": .008,
            "Bildu": .008,
            "CC": .003
        },
        "Winnable-Ideologia": {
            "PP": .192,
            "PSOE": .172,
            "Podemos": .117,
            "C's": .106,
            "ERC": .067,
            "DiL": .089,
            "PNV": .088,
            "IU": .043,
            "Bildu": .053,
            "CC": .074
        },
        "Worsable-Ideologia": {
            "PP": .156,
            "PSOE": .203,
            "Podemos": .101,
            "C's": .110,
            "ERC": .062,
            "DiL": .097,
            "PNV": .098,
            "IU": .036,
            "Bildu": .050,
            "CC": .086
        }
    }

    return jsonify(data)


if __name__ == "__main__":
    ## Run app
    app.run(debug=True, host='0.0.0.0', port=5000)

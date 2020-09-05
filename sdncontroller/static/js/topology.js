var $srtopology = (function() {

    var record_path = false;
    var label_path = $('#label_path');
    var recordPathBtn = $('#recordPathBtn');
    var clearPathBtn = $('#clearPathBtn');
    var deployBtn = $('#deployBtn');

    var prefix = $('#prefixInput');
    var nexthop = $('#nexthopInput');

    var label_array = [];

    var display_nodes = new vis.DataSet(topology_details["nodes"]);
      
    var edges = new vis.DataSet(topology_details["edges"])

    // create a network
    var container = document.getElementById("topology");
    var data = {
      nodes: display_nodes,
      edges: edges
    };

    var options = {
        interaction: { hover: true, selectConnectedEdges: false },
      manipulation: {
        enabled: true,
      },
    };

    var network = new vis.Network(container, data, options);
    
    network.on('click', function(e) {onClick(e)});
    function onClick(e){
        if (record_path){
            if (Array.isArray(e.nodes) && e.nodes.length == 1){
                var current_node_label = getNodeSRLabel(e);
                label_path.append(current_node_label + " ---> ");
                label_array.push(current_node_label);
            }
            
            if (Array.isArray(e.edges) && e.edges.length == 1){
                var current_link_label = getEdgeSRLabel(e);
                label_path.append(current_link_label + " ---> ");
                label_array.push(current_link_label);
            }
            console.log("Current label stack path is: " + label_array)
            //console.log(e);
        }
    }

    function getNodeSRLabel(data){
        node_id = data.nodes[0];
        node = display_nodes.get(node_id);
        console.log("Node: " + node.sr_labels);
        return node.sr_labels[0];
    }

    function getEdgeSRLabel(data){
        //console.log("Link: " + data.edges[0]);
        edge_id = data.edges[0];
        edge = edges.get(edge_id);
        console.log("Link: " + edge.label);
        return edge.label;
    }

    function enablePathRecord(){
        if(record_path == true){
            recordPathBtn.html("Record Path");
            recordPathBtn.removeClass('btn-danger');
            recordPathBtn.addClass('btn-primary');
            label_path.append(" Done")
            record_path = false;
            return;
        }
        resetLabelPath();
        recordPathBtn.html("Recording...");
        recordPathBtn.removeClass('btn-primary');
        recordPathBtn.addClass('btn-danger');
        record_path = true;
        return;
    }

    function clearPath(){
        label_path.empty();
        label_path.html("Label Path: ");
        resetLabelPath();
    }

    function resetLabelPath(){
        if(label_array.length){
            label_array = [];
        }
    }

    function deployPrefix(){
        if(record_path == true){
            alert("Path is still being recorded...");
            return;
        }

        if(label_array.length == 0){
            alert("Label path is 0... Please record a path...");
            return;
        }

        $.ajax({
            method: "POST",
            url: "/api/v1/deploy",
            data: JSON.stringify({
                "prefix": prefix.val(),
                "nexthop": nexthop.val(),
                "label_path": label_array
            }),
            headers: {"Content-Type": "application/json"}
        }).done(function (data){
            console.log(data);
        }).fail(function (jqXHR, textStatus, errorThrown) {
            console.log(errorThrown);
        });

        console.log("Deploying Prefix: " + prefix.val() + " with nexthop: " + nexthop.val());
    }

    recordPathBtn.on('click', function(e){
        e.preventDefault();
        enablePathRecord();
        console.log(record_path);
    });

    clearPathBtn.on('click', function(e){
        e.preventDefault();
        if(record_path){
            enablePathRecord();
        }
        clearPath();
    });

    deployBtn.on('click', function(e){
        e.preventDefault();
        deployPrefix();
    });

})();

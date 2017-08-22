define(['base/js/namespace', 'base/js/utils', 'jquery'], function(Jupyter, utils, $) {
    function create_toc_text() {
        var toc_text = "# Table of Contents\n";
        var cells = Jupyter.notebook.get_cells();
        var heading_count = 0;
        for (var i = 0; i < cells.length; i++) {
            var cell = cells[i];
            if (cell.cell_type == "markdown") {
               var cell_content = cell.get_text(); 
               if (cell_content.startsWith("#") & cell_content.indexOf('Table of Contents')) {
                   // Increment the heading count
                   heading_count++;
                   // Get the heading title
                   var last_hash = cell_content.lastIndexOf("#");
                   var hash_num = last_hash + 1;
                   var heading_title = cell_content.substr(hash_num);
                   // Clean up the existing heading content
                   var first_tag = heading_title.indexOf("<");
                   if (first_tag != -1) {
                       heading_title = heading_title.slice(0, first_tag);
                   }
                   // Create a <a> tag for linking to fragment
                   var link_fragment_heading = heading_title.toLowerCase().replace(" ", "_");
                   var link_fragment = '<a name="' + link_fragment_heading + '"></a>';
                   // Append the <a> tag to the heading cell
                   cell.set_text(cell.get_text() +  link_fragment);
                   cell.render();
                   // Add the heading to the TOC cell
                   toc_text += (Array(hash_num).join('  ') + '- ');
                   toc_text += ("[" + heading_title + "](#" + link_fragment_heading + ") \n");
               }
            }
        }
        return toc_text;
    }

    function load_toc_cell(toc_cell, toc_text) {
        if (toc_cell == null) {
            var toc_cell = Jupyter.notebook.insert_cell_at_index('markdown', 0);
        }
        toc_cell.set_text(toc_text);
        toc_cell.render();
    }

    function create_toc() {
        var toc_text = create_toc_text();
        load_toc_cell(null, toc_text);
    }

    function refresh_toc() {
        var toc_text = create_toc_text();
        load_toc_cell(Jupyter.notebook.get_cell(0), toc_text);
    }

    function place_toc_button() {
        if (!Jupyter.toolbar) {
            $([Jupyter.events]).on("app_initialized.NotebookApp", place_toc_button);
            return;
        }

        if ($("#create-toc-button").length == 0) {
            Jupyter.toolbar.add_buttons_group([
                {
                    'label': 'Create Table of Contents',
                    'icon': 'fa-table',
                    'callback': create_toc,
                    'id': 'create-toc-button'
                },
                {
                    'label': 'Refresh Table of Contents',
                    'icon': 'fa-refresh',
                    'callback': refresh_toc,
                    'id': 'refresh-toc-button'
                },
            ]);
        }
    }

    function load_ipython_extension() {
        console.log('Loading notebook-toc extension...');
        place_toc_button();
    }

    return {
        load_ipython_extension: load_ipython_extension
    };
});

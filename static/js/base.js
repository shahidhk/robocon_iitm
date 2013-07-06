// MAJOR DIV HANDLING
function js_alert_show(alert_type, alert_msg) { // Alert type = success, info, error, warning
    // To show an alert using javascript
    // Note : this is redundant after the show_alert in misc.utilities was made
    document.getElementById('id_alert').className = 'alert alert-' + alert_type.toLowerCase();
    document.getElementById('id_alert').innerHTML = '<button onclick="javascript:js_alert_hide();">&times;</button>' +
        '<strong>' + alert_type.toUpperCase() + '!</strong> ' + alert_msg;
}

function js_alert_hide() {
    // Hide the alert with javascript
    // Note : this is used for the cross close button in the alert div
    document.getElementById('id_alert').className = 'alert hide';
    document.getElementById('id_alert').innerHTML = '';
}

function modal_hide() {
    // Hides the modal which is used for temp views
    $('#id_modal').addClass('hide');
    //$('#id_modal').html('');
    
    /* On hiding modal, refresh the page's right content based on which 
        tab is active on the left_content
        * this is done by "virtually calling the click function" ... 
    */
}

// Shows a loading.gif and later displays when dajax responds
function do_dajax(_dajax_func, _handler_func, _args, _id_content) {
    // _func is the Dajax function to call
    // _handler_func is the function to call after Dajaxice gives the json
    // _args is the arguments to give to Dajax function
    // _id_content is the id which needs to be populated
    jq_obj = $("#" + _id_content)
    if( _id_content == "id_modal" ) { // if id is the global modal show it !
        // Set innerHTML of div to LOADING
        html_content =  '<center>';
        html_content +=   '<div class="modal-header">';
        html_content +=     '<button type="button" class="close" onclick="javascript:modal_hide()">&times;</button>'
        html_content +=     '<h3>Loading...</h3>'
        html_content +=   '</div>'
        html_content +=   '<div class="modal-body" >'
        html_content +=     '<img src="/static/img/loading.gif" />'
        html_content +=   '</div>'
        html_content += '</center>'
        jq_obj.html(html_content)
        jq_obj.removeClass("hide") // show modal
    } else {
        html_content =  '<center>'
        html_content +=     '<img src="/static/img/loading.gif" />'
        html_content += '</center>'
        jq_obj.html(html_content)
    }
        
    
    // TELL DAJAX TO GIVE
    //_args['id_content'] = _id_content // put in the id_content provided
    _dajax_func(_handler_func, _args)
}


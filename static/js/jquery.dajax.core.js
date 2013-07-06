/* Copyright (c) 2009-2010, Benito Jorge Bastida :: For further information check COPYING */
var Dajax = {
    process: function(data)
    {
        if(data==Dajaxice.EXCEPTION){
            alert('Something went wrong, please reload the page.');
        }
        else{
            $.each(data, function(i,elem){
            switch(elem.cmd)
            {
                case 'alert':
                    alert(elem.val.toString())
                break;
        
                case 'data':
                    eval( elem.fun.toString()+"(elem.val.toString());" );
                break;
        
                case 'as':
                    jQuery.each($(elem.id.toString()),function(){ this[elem.prop.toString()] = elem.val.toString(); });
                break;
        
                case 'addcc':
                    jQuery.each(elem.val,function(){
                        $(elem.id.toString()).addClass(this.toString());
                    });
                break;
            
                case 'remcc':
                    jQuery.each(elem.val,function(){
                        $(elem.id.toString()).removeClass(this.toString());
                    });
                break;
            
                case 'ap':
                    jQuery.each($(elem.id.toString()),function(){ this[elem.prop.toString()] += elem.val.toString(); });
                break;
            
                case 'pp':
                    jQuery.each($(elem.id.toString()),function(){ this[elem.prop.toString()] = elem.val.toString() + this[elem.prop.toString()]; });
                break;
            
                case 'clr':
                    jQuery.each($(elem.id.toString()),function(){ this[elem.prop.toString()] = ""; });
                break;
            
                case 'red':
                    window.setTimeout('window.location="'+elem.url.toString()+'";',elem.delay);
                break;
            
                case 'js':
                    eval(elem.val.toString());
                break;
            
                case 'rm':
                    $(elem.id.toString()).remove();
                break;
            
                default:
                    alert('Unknown action!');
                }
            });
        }
    }
};

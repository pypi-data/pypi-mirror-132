jQuery(function($) {
    'use strict';

    let $positionSelection = $('#id_position');
    let $fmi = $('.field-mobile_image')
    let $imi = $('#id_mobile_image')
    let $fsmi = $('.field-small_mobile_image')
    let $ismi = $('#id_small_mobile_image')

    function changePositionSelection() {

        switch ($positionSelection.val()){
            case 'TOP' :
                $fmi.show();
                $fsmi.hide();
                $imi.prop('disabled', false);
                $ismi.prop('disabled', true);
                break;
            case 'SDL':
            case 'SDR':
                $fmi.hide();
                $fsmi.hide();
                $imi.prop('disabled', true);
                $ismi.prop('disabled', true);
                break;
            case 'CON':
            case 'BOT':
                $fmi.hide();
                $fsmi.show();
                $imi.prop('disabled', true);
                $ismi.prop('disabled', false);
                break;
        }
    }

    $positionSelection.on('change', changePositionSelection);
    changePositionSelection();
});
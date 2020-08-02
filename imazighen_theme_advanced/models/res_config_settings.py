# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models
import pathlib
import logging
_logger = logging.getLogger(__name__)
import re
import urllib, os 
import zeep

default_colors = {'main_menu_color'    :'#875A7B',
                'premary_btn_color'    :'#00A09D',
                'list_view_header'     :'#FFFFFF',
                'list_footer_bg_color' :'#FFFFFF', 
                'webclient_background' :'#ebe8e8',
                'view_background_color':'#FFFFFF',
                'main_text_color'      :'#4c4c4c',
                'home_menu_background_from'      :'#77717e',
                'home_menu_background_to'      :'#c9a8a9',

}

class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    main_menu_color              = fields.Char('Main menu color',)
    premary_btn_color            = fields.Char('Primary button color',)
    list_view_header             = fields.Char('List view header color',)
    list_footer_bg_color         = fields.Char('List footer bg color',)
    webclient_background         = fields.Char('Webclient background color',)
    view_background_color        = fields.Char('View background color',)
    main_text_color              = fields.Char('Main text color',)
    home_menu_background_from    = fields.Char('Home menu background from',)
    home_menu_background_to      = fields.Char('Home menu background from',)

    def load_default_colorhome_menu_background(self,):
        self.env['ir.config_parameter'].set_param('home_menu_background_from', default_colors['home_menu_background_from'])
        self.env['ir.config_parameter'].set_param('home_menu_background_to', default_colors['home_menu_background_to'])
        

    def load_default_color_main_menu_color(self,):
        self.env['ir.config_parameter'].set_param('main_menu_color', default_colors['main_menu_color'])

    def load_default_color_premary_btn_color(self,):
        self.env['ir.config_parameter'].set_param('premary_btn_color', default_colors['premary_btn_color'])

    def load_default_color_list_view_header(self,):
        self.env['ir.config_parameter'].set_param('list_view_header', default_colors['list_view_header'])

    def load_default_color_list_footer_bg_color(self,):
        self.env['ir.config_parameter'].set_param('list_footer_bg_color', default_colors['list_footer_bg_color'])

    def load_default_color_webclient_background(self,):
        self.env['ir.config_parameter'].set_param('webclient_background', default_colors['webclient_background'])

    def load_default_color_view_background_color(self,):
        self.env['ir.config_parameter'].set_param('view_background_color', default_colors['view_background_color'])
    
    def load_default_color_main_text_color(self,):
        self.env['ir.config_parameter'].set_param('main_text_color', default_colors['main_text_color'])


    
    def change_sccs_file_primary_variables(self,params):
        _logger.warning('\n ok ok params=>%s',params)
        path=str(pathlib.Path(__file__).parent.absolute()).replace("models","static/src/scss/primary_variables.scss") 
        filedata = None
        with open(path, 'r') as file:
            filedata = file.read()  
       
      
        new_file_data = str(filedata).replace(str(re.search('(.*)o-brand-odoo(.*);', filedata)[0]),'$o-brand-odoo:'+params["main_menu_color"]+';') 
        new_file_data = new_file_data.replace(str(re.search('(.*)o-brand-primary(.*);', filedata)[0]),'$o-brand-primary:'+params["premary_btn_color"]+';') 
        new_file_data = new_file_data.replace(str(re.search('(.*)liste_view_thead_thead_colors(.*);', filedata)[0]),'$liste_view_thead_thead_colors:'+params["list_view_header"]+';')
        new_file_data = new_file_data.replace(str(re.search('(.*)o-list-footer-bg-color(.*);', filedata)[0]),'$o-list-footer-bg-color:'+params["list_footer_bg_color"]+';')
        new_file_data = new_file_data.replace(str(re.search('(.*)o-webclient-background-color(.*);', filedata)[0]),'$o-webclient-background-color:'+params["webclient_background"]+';')
        new_file_data = new_file_data.replace(str(re.search('(.*)o-view-background-color(.*);', filedata)[0]),'$o-view-background-color:'+params["view_background_color"]+';')
        new_file_data = new_file_data.replace(str(re.search('(.*)o-main-text-color(.*);', filedata)[0]),'$o-main-text-color:'+params["main_text_color"]+';')

        new_file_data = new_file_data.replace(str(re.search('(.*)home_menu_background_from(.*);', filedata)[0]),'$home_menu_background_from:'+params["home_menu_background_from"]+';')
        new_file_data = new_file_data.replace(str(re.search('(.*)home_menu_background_to(.*);', filedata)[0]),'$home_menu_background_to:'+params["home_menu_background_to"]+';')

        with open(path, "w") as f:
            f.write(new_file_data)


    @api.model
    def get_values(self):
        res = super(ResConfigSettings, self).get_values()
        res.update(
            main_menu_color         = self.env['ir.config_parameter'].get_param('main_menu_color'),
            premary_btn_color       = self.env['ir.config_parameter'].get_param('premary_btn_color'),
            list_view_header        = self.env['ir.config_parameter'].get_param('list_view_header'),
            list_footer_bg_color    = self.env['ir.config_parameter'].get_param('list_footer_bg_color'),
            webclient_background    = self.env['ir.config_parameter'].get_param('webclient_background'),
            view_background_color   = self.env['ir.config_parameter'].get_param('view_background_color'),
            main_text_color         = self.env['ir.config_parameter'].get_param('main_text_color'),
            home_menu_background_from      = self.env['ir.config_parameter'].get_param('home_menu_background_from'),
            home_menu_background_to        = self.env['ir.config_parameter'].get_param('home_menu_background_to'),
        )
        return res

    def set_values(self):
        params={}
        res = super(ResConfigSettings, self).set_values()
        self.env['ir.config_parameter'].set_param('main_menu_color', self.main_menu_color)
        self.env['ir.config_parameter'].set_param('premary_btn_color', self.premary_btn_color)
        self.env['ir.config_parameter'].set_param('list_view_header', self.list_view_header)
        self.env['ir.config_parameter'].set_param('list_footer_bg_color', self.list_view_header)
        self.env['ir.config_parameter'].set_param('webclient_background', self.webclient_background)
        self.env['ir.config_parameter'].set_param('view_background_color', self.view_background_color)
        self.env['ir.config_parameter'].set_param('main_text_color', self.main_text_color)
        self.env['ir.config_parameter'].set_param('home_menu_background_from', self.home_menu_background_from)
        self.env['ir.config_parameter'].set_param('home_menu_background_to', self.home_menu_background_to)
        params['main_menu_color']        = self.main_menu_color
        params['premary_btn_color']      = self.premary_btn_color
        params['list_view_header']       = self.list_view_header
        params['list_footer_bg_color']   = self.list_footer_bg_color
        params['webclient_background']   = self.webclient_background
        params['view_background_color']  = self.view_background_color
        params['main_text_color']        = self.main_text_color
        params['home_menu_background_from']      = self.home_menu_background_from
        params['home_menu_background_to']        = self.home_menu_background_to

        self.change_sccs_file_primary_variables(params)
       


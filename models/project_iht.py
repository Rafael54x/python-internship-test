from odoo import models, fields

class ProjectIHT(models.Model):
    _inherit = 'project.project'

    lokasi_proyek = fields.Text("Lokasi Proyek")
    source_aplikasi_pendukung = fields.Char("Source Aplikasi Pendukung")
    daftar_pekerja_remote = fields.Json("Daftar Pekerja Remote")

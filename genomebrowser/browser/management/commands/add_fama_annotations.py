import os
from django.core.management.base import BaseCommand
from browser.models import *
from browser.dataimport.annotator import Annotator

class Command(BaseCommand):
    help = 'For protein sequences uploaded to Django database, this program finds Fama annotations in all_proteins.list.txt file generated by Fama and writes the annotations to the database'

    def add_arguments(self, parser):
        parser.add_argument('-i', default='all_proteins.list.txt', help='Path to Fama output file')

    def handle(self, *args, **options):
        annotator = Annotator()
        annotator.add_fama_annotations(options['i'])

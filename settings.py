import os
here = lambda *x: os.path.join(os.path.abspath(os.path.dirname(__file__)), *x)

#Directories
LAYOUT_DIR = here('layout')
CONTENT_DIR = here('content')
MEDIA_DIR = here('media')
DEPLOY_DIR = here('deploy')
TMP_DIR = here('deploy_tmp')

BACKUPS_DIR = here('backups')
BACKUP = False

SITE_ROOT = "/"
SITE_WWW_URL = "http://www.JasonSidabras.com"
SITE_NAME = "Jason W. Sidabras"
SITE_AUTHOR = "Jason W. Sidabras"

#URL Configuration
GENERATE_ABSOLUTE_FS_URLS = False

# Clean urls causes Hyde to generate urls without extensions. Examples:
# http://example.com/section/page.html becomes
# http://example.com/section/page/, and the listing for that section becomes
# http://example.com/section/
# The built-in CherryPy webserver is capable of serving pages with clean urls
# without any additional configuration, but Apache will need to use Mod_Rewrite
# to map the clean urls to the actual html files.  The HtaccessGenerator site
# post processor is capable of automatically generating the necessary
# RewriteRules for use with Apache.
GENERATE_CLEAN_URLS = False

# A list of filenames (without extensions) that will be considered listing
# pages for their enclosing folders.
# LISTING_PAGE_NAMES = ['index']
LISTING_PAGE_NAMES = ['listing', 'index', 'default']

# Determines whether or not to append a trailing slash to generated urls when
# clean urls are enabled.
APPEND_SLASH = False

# {folder : extension : (processors)}
# The processors are run in the given order and are chained.
# Only a lone * is supported as an indicator for folders. Path
# should be specified. No wildcard card support yet.

# Starting under the media folder. For example, if you have media/css under
# your site root,you should specify just css. If you have media/css/ie you
# should specify css/ie for the folder name. css/* is not supported (yet).

# Extensions do not support wildcards.

MEDIA_PROCESSORS = {
    '*':{
        '.css':('hydeengine.media_processors.TemplateProcessor',
                'hydeengine.media_processors.CSSmin',),
        '.ccss':('hydeengine.media_processors.TemplateProcessor',
                'hydeengine.media_processors.CleverCSS',
                'hydeengine.media_processors.CSSmin',),
        '.sass':('hydeengine.media_processors.TemplateProcessor',
                'hydeengine.media_processors.SASS',
                'hydeengine.media_processors.CSSmin',),
        '.less':('hydeengine.media_processors.TemplateProcessor',
                'hydeengine.media_processors.LessCSS',
                'hydeengine.media_processors.CSSmin',),
        '.styl':('hydeengine.media_processors.TemplateProcessor',
                'hydeengine.media_processors.Stylus',
                'hydeengine.media_processors.CSSmin',),
        '.hss':(
                'hydeengine.media_processors.TemplateProcessor',
                'hydeengine.media_processors.HSS',
                'hydeengine.media_processors.CSSmin',),
        '.js':(
                'hydeengine.media_processors.TemplateProcessor',
                'hydeengine.media_processors.JSmin',),
        '.coffee':(
                'hydeengine.media_processors.TemplateProcessor',
                'hydeengine.media_processors.CoffeeScript',
                'hydeengine.media_processors.JSmin',)
    }
}

CONTENT_PROCESSORS = {
    'prerendered/': {
        '*.*' :
            ('hydeengine.content_processors.PassthroughProcessor',)
            }
}

SITE_POST_PROCESSORS = {
    # 'media/js': {
    #        'hydeengine.site_post_processors.FolderFlattener' : {
    #                'remove_processed_folders': True,
    #                'pattern':"*.js"
    #        }
    #    }
}

CONTEXT = {
    'GENERATE_CLEAN_URLS': GENERATE_CLEAN_URLS
}

FILTER = {
    'include': (".htaccess",),
    'exclude': (".*","*~")
}


#Processor Configuration

#
#  Set this to the output of `which growlnotify`. If `which`  returns emtpy,
#  install growlnotify from the Extras package that comes with the Growl disk image.
#
#
GROWL = None

# path for YUICompressor, or None if you don't
# want to compress JS/CSS. Project homepage:
# http://developer.yahoo.com/yui/compressor/
#YUI_COMPRESSOR = "./lib/yuicompressor-2.4.2.jar"
YUI_COMPRESSOR = None

# path for Closure Compiler, or None if you don't
# want to compress JS/CSS. Project homepage:
# http://closure-compiler.googlecode.com/
#CLOSURE_COMPILER = "./lib/compiler.jar"
CLOSURE_COMPRILER = None

# path for HSS, which is a preprocessor for CSS-like files (*.hss)
# project page at http://ncannasse.fr/projects/hss
#HSS_PATH = "./lib/hss-1.0-osx"
HSS_PATH = None # if you don't want to use HSS

#Django settings

TEMPLATE_DIRS = (LAYOUT_DIR, CONTENT_DIR, TMP_DIR, MEDIA_DIR)

INSTALLED_APPS = (
    'hydeengine',
    'django.contrib.webdesign',
)

CATEGORY_ARCHIVES_DIR = "archives"
SITE_PRE_PROCESSORS = {
    'blog': {
        'hydeengine.site_pre_processors.CategoriesManager' : {
            # blog.categories gets populated even if there are no other
            # settings here.

            # Key 'archiving':
            #
            # Whether to produce any lists --- per-category lists of posts and
            # perhaps an all-category list.
            #
            # Optional.  Default: False
            #
            # If True, category templates (configured below) will be expanded
            # to produce pages.
            #
            # If False, blog.categories gets populated as usual but nothing
            # else happens (no output is produced, even if template
            # names/output directories are configured).
            #
            # Presumably called 'archives' because one application of
            # categories is to put every blog in a category named after the
            # year it got posted.
            'archiving': True,

            # Key 'template':
            #
            # The template to expand once per unique category, relative to
            # LAYOUT_DIR.
            #
            # Mandatory if archiving is True.
            #
            # Gets passed 'posts' and 'categories'.  Typically you'll code this
            # template to expand to a list of all pages in the given category.
            # Depending on whether you use clean URLs, produces either:
            #    <category>.html
            # or:
            #    <category>/index.html
            # for each category.
            'template': '_per_category.html',

            # Key 'output_folder'
            #
            # The directory to write per-unique-category pages to.
            #
            # Optional.  Default: the value of CATEGORY_ARCHIVES_DIR if set,
            # else the string 'archives'.
            'output_folder': 'category',

            # Key 'listing_template':
            #
            # The template to expand just once.
            #
            # Optional.  Default: not generated
            #
            # Gets passed 'categories'.  Typically used to generate a list of
            # all categories.  You can achieve the same thing in any page
            # without this by obtaining a reference to <node>.categories,
            # perhaps with the help of the node injection preprocessor.
            'listing_template': '_category_index.html',

            # Key 'meta':
            #
            # A dictionary of category metadata, typically used to describe
            # each category.
            #
            # Optional.  Default: no extra properties are set
            #
            # Any key-value pairs set here can be accessed as siblings of the
            # automatic properties (category.name, category.posts) e.g. as
            # category.description.
            'meta': {
                'personal': {
                    'description': "Posts related to general personal work.",
                },
                'mortality': {
                    'description': "Posts that remind us how fragile life is",
                },
            },
        },
    },
    '/': {
        'hydeengine.site_pre_processors.NodeInjector' : {
               'variable' : 'blog_node',
               'path' : 'blog'
        }
    },
}          


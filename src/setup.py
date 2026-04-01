from setuptools import setup
import setup_translate

pkg = 'SystemPlugins.AudioEffect'
setup(name='enigma2-plugin-systemplugins-audioeffect',
       version='3.0',
       description='Audio Effect setup',
       package_dir={pkg: 'AudioEffect'},
       packages=[pkg],
       package_data={pkg: ['images/*.png', '*.png', '*.xml', 'locale/*/LC_MESSAGES/*.mo', 'keymap.xml']},
       cmdclass=setup_translate.cmdclass,  # for translation
      )

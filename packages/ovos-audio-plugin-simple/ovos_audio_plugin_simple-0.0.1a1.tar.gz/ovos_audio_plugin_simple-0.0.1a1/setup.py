#!/usr/bin/env python3
from setuptools import setup


PLUGIN_ENTRY_POINT = 'ovos_audio_simple=ovos_audio_plugin_simple'

setup(
    name='ovos_audio_plugin_simple',
    version='0.0.1a1',
    description='simple audio plugin for ovos',
    url='https://github.com/OpenVoiceOS/ovos-audio-plugin-simple',
    author='JarbasAi',
    author_email='jarbasai@mailfence.com',
    license='Apache-2.0',
    packages=['ovos_audio_plugin_simple'],
    install_requires=["ovos-plugin-manager>=0.0.1a3"],
    zip_safe=True,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Text Processing :: Linguistic',
        'License :: OSI Approved :: Apache Software License',

        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.0',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    keywords='ovos audio plugin',
    entry_points={'mycroft.plugin.audioservice': PLUGIN_ENTRY_POINT}
)

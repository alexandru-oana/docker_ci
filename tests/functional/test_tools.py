# -*- coding: utf-8 -*-
# Copyright (C) 2021 Intel Corporation
# SPDX-License-Identifier: Apache-2.0
import pytest


@pytest.mark.usefixtures('_is_image_os', '_is_distribution')
class TestTools:
    @pytest.mark.parametrize('_is_image_os', [('ubuntu18', 'ubuntu20')], indirect=True)
    @pytest.mark.parametrize('_is_distribution', [('dev', 'proprietary')], indirect=True)
    def test_accuracy_checker(self, tester, image):
        kwargs = {'mem_limit': '3g'}
        tester.test_docker_image(
            image,
            ['/bin/bash -ac ". /opt/intel/openvino/bin/setupvars.sh && '
             'accuracy_check -h"'],
            self.test_accuracy_checker.__name__, **kwargs,
        )

    @pytest.mark.parametrize('_is_image_os', [('ubuntu18', 'ubuntu20')], indirect=True)
    @pytest.mark.parametrize('_is_distribution', [('dev', 'proprietary')], indirect=True)
    def test_benchmark(self, tester, image):
        kwargs = {'mem_limit': '3g'}
        tester.test_docker_image(
            image,
            ['/bin/bash -ac ". /opt/intel/openvino/bin/setupvars.sh && '
             'cd /opt/intel/openvino/deployment_tools/tools/benchmark_tool && '
             'python3 benchmark_app.py -h"'],
            self.test_benchmark.__name__, **kwargs,
        )

    @pytest.mark.parametrize('_is_image_os', [('ubuntu18', 'ubuntu20', 'centos7')], indirect=True)
    @pytest.mark.parametrize('_is_distribution', [('runtime', 'dev', 'proprietary')], indirect=True)
    def test_cl_compiler(self, tester, image):
        kwargs = {'mem_limit': '3g'}
        tester.test_docker_image(
            image,
            ['/bin/bash -ac ". /opt/intel/openvino/bin/setupvars.sh && '
             'cd /opt/intel/openvino/deployment_tools/tools/cl_compiler/bin && '
             './clc -h"'],
            self.test_cl_compiler.__name__, **kwargs,
        )

    @pytest.mark.parametrize('_is_image_os', [('ubuntu18', 'ubuntu20', 'centos7', 'centos8', 'rhel8')], indirect=True)
    @pytest.mark.parametrize('_is_distribution', [('runtime', 'dev', 'proprietary')], indirect=True)
    def test_compile_tool(self, tester, image):
        kwargs = {'mem_limit': '3g'}
        tester.test_docker_image(
            image,
            ['/bin/bash -ac ". /opt/intel/openvino/bin/setupvars.sh && '
             'cd /opt/intel/openvino/deployment_tools/tools/compile_tool && '
             './compile_tool -h"'],
            self.test_compile_tool.__name__, **kwargs,
        )

    @pytest.mark.parametrize('_is_image_os', [('ubuntu18', 'ubuntu20')], indirect=True)
    @pytest.mark.parametrize('_is_distribution', [('dev', 'proprietary')], indirect=True)
    def test_cross_check_tool(self, tester, image):
        kwargs = {'mem_limit': '3g'}
        tester.test_docker_image(
            image,
            ['/bin/bash -ac ". /opt/intel/openvino/bin/setupvars.sh && '
             'cd /opt/intel/openvino/deployment_tools/tools/cross_check_tool && '
             'python3 cross_check_tool.py -h"'],
            self.test_cross_check_tool.__name__, **kwargs,
        )

    @pytest.mark.parametrize('_is_image_os', [('ubuntu18', 'ubuntu20')], indirect=True)
    @pytest.mark.parametrize('_is_distribution', [('dev', 'proprietary')], indirect=True)
    def test_deployment_manager(self, tester, image):
        kwargs = {'mem_limit': '3g'}
        tester.test_docker_image(
            image,
            ['/bin/bash -ac ". /opt/intel/openvino/bin/setupvars.sh && '
             'cd /opt/intel/openvino/deployment_tools/tools/deployment_manager && '
             'python3 deployment_manager.py -h"'],
            self.test_deployment_manager.__name__, **kwargs,
        )

    @pytest.mark.parametrize('_is_image_os', [('ubuntu18', 'ubuntu20')], indirect=True)
    @pytest.mark.parametrize('_is_distribution', [('dev', 'proprietary')], indirect=True)
    def test_pot(self, tester, image):
        kwargs = {'mem_limit': '3g'}
        tester.test_docker_image(
            image,
            ['/bin/bash -ac ". /opt/intel/openvino/bin/setupvars.sh && '
             'pot --help"'],
            self.test_pot.__name__, **kwargs,
        )
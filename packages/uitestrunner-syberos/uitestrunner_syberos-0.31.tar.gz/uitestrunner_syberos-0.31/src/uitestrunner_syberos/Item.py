# Copyright (C) <2021>  YUANXIN INFORMATION TECHNOLOGY GROUP CO.LTD and Jinzhe Wang
# This file is part of uitestrunner_syberos
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
import base64
import time
from ctypes import *
import threading
import sympy as sp
import math
from lxml import etree
import cv2
import xml.dom.minidom
import numpy as np
import random
from time import sleep
import io
from .DataStruct import *


html_string_1 = "<!DOCTYPE html><html lang=\"en\"><head><meta charset=\"UTF-8\"><title>render</title></head><body style=\"background:#000;clip:rect(auto,auto,auto,auto);\"><div id=\"content\" style=\"width:"
html_string_2 = "px;height:"
html_string_3 = "px;clip:rect(auto,auto,auto,auto);\">"
html_string_4 = "</div></body></html>"


class WorkerThread(threading.Thread):

    result = None

    def __init__(self, func, args=()):
        super(WorkerThread, self).__init__()
        self.func = func
        self.args = args

    def run(self) -> None:
        self.result = self.func(*self.args)

    def get_result(self):
        return self.result


class Item:
    node = None
    xpath = ""
    device = None
    sopid = ""
    __display_width = 0
    __display_height = 0
    rect = []

    def __init__(self, d=None, s="", xpath=""):
        self.sopid = s
        self.device = d
        self.__display_width = self.device.display_width()
        self.__display_height = self.device.display_height()
        self.xpath = xpath
        self.__refresh_node()

    def __refresh_node(self):
        self.node = None
        self.device.refresh_layout()
        selector = etree.XML(self.device.xmlStr.encode('utf-8'))
        nodes = selector.xpath(self.xpath)
        if len(nodes) > 0 and selector.get("sopId") == self.sopid:
            self.node = nodes[0]
            self.__refresh_attribute()
        else:
            self.__init_attribute()

    def __refresh_attribute(self):
        self.__x = int(round(float(self.node.get("x"))))
        self.__y = int(round(float(self.node.get("y"))))
        self.__center_x_to_item = int(round(float(self.node.get("centerXToItem"))))
        self.__center_y_to_item = int(round(float(self.node.get("centerYToItem"))))
        self.__center_x_to_global = int(round(float(self.node.get("centerXToGlobal"))))
        self.__center_y_to_global = int(round(float(self.node.get("centerYToGlobal"))))
        self.__z = int(self.node.get("z"))
        self.__height = int(round(float(self.node.get("height"))))
        self.__width = int(round(float(self.node.get("width"))))
        self.__tempId = self.node.get("tempID")
        self.__text = self.node.get("text")
        self.__objectName = self.node.get("objectName")
        self.__className = self.node.tag
        self.__opacity = float(self.node.get("opacity"))
        self.__enabled = bool(int(self.node.get("enabled")))
        self.__visible = bool(int(self.node.get("visible")))
        self.__focus = bool(int(self.node.get("focus")))
        self.__scale = float(self.node.get("scale"))
        self.__rotation = int(self.node.get("rotation"))
        self.__clip = bool(int(self.node.get("clip")))
        self.__has_contents = bool(int(self.node.get("hasContents")))

    def __init_attribute(self):
        self.__text = str()
        self.__tempId = str()
        self.__x = int()
        self.__y = int()
        self.__z = int()
        self.__center_x_to_item = int()
        self.__center_y_to_item = int()
        self.__center_x_to_global = int()
        self.__center_y_to_global = int()
        self.__height = int()
        self.__width = int()
        self.__className = str()
        self.__objectName = str()
        self.__opacity = float()
        self.__focus = bool()
        self.__enabled = bool()
        self.__visible = bool()
        self.__scale = float()
        self.__rotation = int()
        self.__clip = bool()
        self.__has_contents = bool()

    def x(self, refresh: bool = False) -> int:
        if refresh:
            self.__refresh_node()
        return self.__x

    def y(self, refresh: bool = False) -> int:
        if refresh:
            self.__refresh_node()
        return self.__y

    def center_x_to_item(self, refresh: bool = False) -> int:
        if refresh:
            self.__refresh_node()
        return self.__center_x_to_item

    def center_y_to_item(self, refresh: bool = False) -> int:
        if refresh:
            self.__refresh_node()
        return self.__center_y_to_item

    def center_x_to_global(self, refresh: bool = False) -> int:
        if refresh:
            self.__refresh_node()
        return self.__center_x_to_global

    def center_y_to_global(self, refresh: bool = False) -> int:
        if refresh:
            self.__refresh_node()
        return self.__center_y_to_global

    def z(self, refresh: bool = False) -> int:
        if refresh:
            self.__refresh_node()
        return self.__z

    def scale(self, refresh: bool = False) -> float:
        if refresh:
            self.__refresh_node()
        return self.__scale

    def rotation(self, refresh: bool = False) -> int:
        if refresh:
            self.__refresh_node()
        return self.__rotation

    def clip(self, refresh: bool = False) -> bool:
        if refresh:
            self.__refresh_node()
        return self.__clip

    def height(self, refresh: bool = False) -> int:
        if refresh:
            self.__refresh_node()
        return self.__height

    def width(self, refresh: bool = False) -> int:
        if refresh:
            self.__refresh_node()
        return self.__width

    def temp_id(self, refresh: bool = False) -> str:
        if refresh:
            self.__refresh_node()
        return self.__tempId

    def text(self, refresh: bool = False) -> str:
        if refresh:
            self.__refresh_node()
        return self.__text

    def object_name(self, refresh: bool = False) -> str:
        if refresh:
            self.__refresh_node()
        return self.__objectName

    def class_name(self, refresh: bool = False) -> str:
        if refresh:
            self.__refresh_node()
        return self.__className

    def opacity(self, refresh: bool = False) -> float:
        if refresh:
            self.__refresh_node()
        return self.__opacity

    def enabled(self, refresh: bool = False) -> bool:
        if refresh:
            self.__refresh_node()
        return self.__enabled

    def visible(self, refresh: bool = False) -> bool:
        if refresh:
            self.__refresh_node()
        return self.__visible

    def focus(self, refresh: bool = False) -> bool:
        if refresh:
            self.__refresh_node()
        return self.__focus

    def exist(self, timeout: int = None) -> bool:
        if timeout is None:
            timeout = self.device.default_timeout
        die_time = int(time.time()) + timeout
        while True:
            self.rect = self.__exist()
            if len(self.rect) > 0:
                return True
            sleep(0.5)
            if int(time.time()) > die_time:
                break
        return False

    def __exist(self):
        self.__refresh_node()
        if self.node is not None and self.__visible and self.__opacity > 0 and self.__scale != 0 and self.__width > 0 and self.__height > 0:
            image = []
            if self.device.control_host_type == 0:
                tree = xml.dom.minidom.parseString(self.device.xmlStr)
                for node in tree.documentElement.childNodes:
                    for n in node.childNodes:
                        if len(image) == 0:
                            image = self.__xml_tree_traversed(n.childNodes, 1)
                        else:
                            image = self.__img_cover(image, self.__xml_tree_traversed(n.childNodes, 1))
            else:
                html_string = self.device.libsr.go(c_char_p(bytes(self.device.xmlStr, "utf-8")),
                                                   c_char_p(bytes(self.__tempId, "utf-8")),
                                                   c_int(self.__display_width),
                                                   c_int(self.__display_height))
                self.device.webdriver.get("data:text/html;charset=utf-8," +
                                          html_string_1 + str(self.__display_width) +
                                          html_string_2 + str(self.__display_height) +
                                          html_string_3 + string_at(html_string, -1).decode('utf-8') +
                                          html_string_4)
                image = cv2.imdecode(np.frombuffer(base64.b64decode(self.device.webdriver.get_screenshot_as_base64()), np.uint8), cv2.COLOR_RGB2BGR)
            # cv2.imshow(str(self.device.system_time()), image)
            # cv2.waitKey(0)
            b, g, r = cv2.split(image)
            if len(np.argwhere(r == 255)) > 0:
                return np.argwhere(r == 255)
        return []

    def __xml_tree_traversed(self, nodes, fs):
        all_images = {}
        th_index = 0
        th_list = {}
        for node in nodes:
            th = WorkerThread(func=self.__draw_item, args=(node, fs, ))
            th_list[th_index] = th
            th.setDaemon(True)
            th_index += 1
        for i in range(th_index):
            th_list[i].start()
        for i in range(th_index):
            th_list[i].join()
            images = th_list[i].get_result()
            for image_z in images:
                if image_z in all_images.keys():
                    all_images[image_z] = self.__img_cover(all_images[image_z], images[image_z])
                else:
                    all_images[image_z] = images[image_z]
        im_list = list(all_images.keys())
        im_list.sort()
        r_image = np.zeros((self.__display_height, self.__display_width), dtype=np.uint8)
        r_image = cv2.cvtColor(r_image, cv2.COLOR_GRAY2BGR)
        for index in im_list:
            r_image = self.__img_cover(r_image, all_images[index])
        return r_image

    def __draw_item(self, node, fs):
        images = {}
        clip = int(node.getAttribute("clip"))
        scale = abs(float(node.getAttribute("scale")) * fs)
        height = round(float(node.getAttribute("height")) * scale)
        width = round(float(node.getAttribute("width")) * scale)
        rotation = 0 - int(node.getAttribute("rotation"))
        has_contents = bool(int(node.getAttribute("hasContents")))
        cx = round(float(node.getAttribute("centerXToGlobal")))
        cy = round(float(node.getAttribute("centerYToGlobal")))
        if height > 10000 or width > 10000:
            x = float(node.getAttribute("x"))
            y = float(node.getAttribute("y"))
            cx, cy, width, height = self.__clip_item(float(cx), float(cy), float(width), float(height), x, y,
                                                     0 - rotation)
        if float(node.getAttribute("opacity")) != 0 \
                and int(node.getAttribute("visible")) == 1 \
                and node.nodeName != "QQuickShaderEffectSource":
            index_z = int(node.getAttribute("z"))
            if height > 0 and width > 0:
                image = np.zeros((height, width), dtype=np.uint8)
            else:
                image = np.zeros((self.__display_height, self.__display_width), dtype=np.uint8)
            image = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
            if has_contents or (node.nodeName == "QQuickLoader" and node.getAttribute("z") == "10000" and
                                node.getAttribute("tempID") == "temp7"):
                if node.getAttribute("tempID") == self.__tempId:
                    cv2.rectangle(image, (0, 0), (width, height), (0, 0, 255), -1)
                else:
                    cv2.rectangle(image, (0, 0), (width, height), (255, 0, 0), -1)
                    # cv2.rectangle(image, (0, 0), (width, height),
                    #              (random.randint(0, 255), 0, random.randint(0, 255)), -1)
            else:
                cv2.rectangle(image, (0, 0), (width, height), (0, 255, 0), -1)
            hypotenuse = int(math.sqrt(height ** 2 + width ** 2))
            M1 = np.float32([[1, 0, (hypotenuse - width) / 2], [0, 1, (hypotenuse - height) / 2]])
            image = cv2.warpAffine(image, M1, (hypotenuse, hypotenuse))
            M2 = cv2.getRotationMatrix2D((hypotenuse / 2, hypotenuse / 2), rotation, 1)
            image = cv2.warpAffine(image, M2, (hypotenuse, hypotenuse))
            M3 = np.float32([[1, 0, cx - (hypotenuse / 2)], [0, 1, cy - (hypotenuse / 2)]])
            image = cv2.warpAffine(image, M3, (self.__display_width, self.__display_height))
            if node.childNodes.length > 0:
                c_images = self.__xml_tree_traversed(node.childNodes, scale)
                image = self.__img_cover(image, c_images, clip)
            if index_z in images.keys():
                images[index_z] = self.__img_cover(images[index_z], image)
            else:
                images[index_z] = image
        return images

    def __clip_item(self, cx, cy, width, height, x, y, rotation):
        if width > 10000:
            r_width = 10000
        else:
            r_width = width
        if height > 10000:
            r_height = 10000
        else:
            r_height = height
        diagonal = math.sqrt(r_height ** 2 + r_width ** 2)
        p1x = x
        p1y = y
        p2x = None
        p2y = None
        p3x = 2 * (cx - x) + x
        p3y = 2 * (cy - y) + y
        p4x = None
        p4y = None
        if rotation % 90 == 0:
            if rotation / 90 % 4 == 0:
                p2x = p3x
                p2y = p1y
                p4x = p1x
                p4y = p3y
            elif rotation / 90 % 4 == 1:
                p2x = p1x
                p2y = p3y
                p4x = p3x
                p4y = p1y
            elif rotation / 90 % 4 == 2:
                p2x = p3x
                p2y = p1y
                p4x = p1x
                p4y = p3y
            elif rotation / 90 % 4 == 3:
                p2x = p1x
                p2y = p3y
                p4x = p3x
                p4y = p1y
        elif 0 < rotation % 360 < 90:
            p2x = p1x + self.__cos(rotation % 90) * width
            p2y = p1y + self.__sin(rotation % 90) * width
            p4x = p1x - self.__cos(90 - (rotation % 90)) * height
            p4y = p1y + self.__sin(90 - (rotation % 90)) * height
        elif 90 < rotation % 360 < 180:
            p2x = p1x - self.__sin(rotation % 90) * width
            p2y = p1y + self.__cos(rotation % 90) * width
            p4x = p1x - self.__sin(90 - (rotation % 90)) * height
            p4y = p1y - self.__cos(90 - (rotation % 90)) * height
        elif 180 < rotation % 360 < 270:
            p2x = p1x - self.__cos(rotation % 90) * width
            p2y = p1y - self.__sin(rotation % 90) * width
            p4x = p1x + self.__cos(90 - (rotation % 90)) * height
            p4y = p1y - self.__sin(90 - (rotation % 90)) * height
        elif 270 < rotation % 360 < 360:
            p2x = p1x + self.__sin(rotation % 90) * width
            p2y = p1y - self.__cos(rotation % 90) * width
            p4x = p1x + self.__sin(90 - (rotation % 90)) * height
            p4y = p1y + self.__cos(90 - (rotation % 90)) * height
        if 0 <= p1x <= self.__display_width and 0 <= p1y <= self.__display_height:
            pwx, pwy, phx, phy = self.__compute_vertex(p1x, p1y, p1x, p1y, p2x, p2y, p4x, p4y, width, height,
                                                       r_width, r_height)
            r_cx = round(pwx + (phx - pwx) / diagonal * (diagonal / 2))
            r_cy = round(pwy + (phy - pwy) / diagonal * (diagonal / 2))
            return int(r_cx), int(r_cy), int(r_width), int(r_height)
        elif 0 <= p2x <= self.__display_width and 0 <= p2y <= self.__display_height:
            pwx, pwy, phx, phy = self.__compute_vertex(p2x, p2y, p2x, p2y, p1x, p1y, p3x, p3y, width, height,
                                                       r_width, r_height)
            r_cx = round(pwx + (phx - pwx) / diagonal * (diagonal / 2))
            r_cy = round(pwy + (phy - pwy) / diagonal * (diagonal / 2))
            return int(r_cx), int(r_cy), int(r_width), int(r_height)
        elif 0 <= p3x <= self.__display_width and 0 <= p3y <= self.__display_height:
            pwx, pwy, phx, phy = self.__compute_vertex(p3x, p3y, p3x, p3y, p4x, p4y, p2x, p2y, width, height,
                                                       r_width, r_height)
            r_cx = round(pwx + (phx - pwx) / diagonal * (diagonal / 2))
            r_cy = round(pwy + (phy - pwy) / diagonal * (diagonal / 2))
            return int(r_cx), int(r_cy), int(r_width), int(r_height)
        elif 0 <= p4x <= self.__display_width and 0 <= p4y <= self.__display_height:
            pwx, pwy, phx, phy = self.__compute_vertex(p4x, p4y, p4x, p4y, p3x, p3y, p1x, p1y, width, height,
                                                       r_width, r_height)
            r_cx = round(pwx + (phx - pwx) / diagonal * (diagonal / 2))
            r_cy = round(pwy + (phy - pwy) / diagonal * (diagonal / 2))
            return int(r_cx), int(r_cy), int(r_width), int(r_height)
        flag, ix, iy = self.__segment_intersect_display(p1x, p1y, p2x, p2y)
        if flag:
            if width > 10000:
                if math.sqrt((ix - p1x) ** 2 + (iy - p1y) ** 2) < 5000:
                    pwx, pwy, phx, phy = self.__compute_vertex(p1x, p1y, p1x, p1y, p2x, p2y, p4x, p4y, width, height,
                                                               r_width, r_height)
                    r_cx = round(pwx + (phx - pwx) / diagonal * (diagonal / 2))
                    r_cy = round(pwy + (phy - pwy) / diagonal * (diagonal / 2))
                    return int(r_cx), int(r_cy), int(r_width), int(r_height)
                elif width - math.sqrt((ix - p1x) ** 2 + (iy - p1y) ** 2) < 5000:
                    pwx, pwy, phx, phy = self.__compute_vertex(p2x, p2y, p2x, p2y, p1x, p1y, p3x, p3y, width, height,
                                                               r_width, r_height)
                    r_cx = round(pwx + (phx - pwx) / diagonal * (diagonal / 2))
                    r_cy = round(pwy + (phy - pwy) / diagonal * (diagonal / 2))
                    return int(r_cx), int(r_cy), int(r_width), int(r_height)
                else:
                    sx = p1x + (p2x - p1x) / width * (math.sqrt((ix - p1x) ** 2 + (iy - p1y) ** 2) - 5000)
                    sy = p1y + (p2y - p1y) / width * (math.sqrt((ix - p1x) ** 2 + (iy - p1y) ** 2) - 5000)
                    pwx, pwy, phx, phy = self.__compute_vertex(sx, sy, p1x, p1y, p2x, p2y, p4x, p4y, width, height,
                                                               r_width, r_height)
                    r_cx = round(pwx + (phx - pwx) / diagonal * (diagonal / 2))
                    r_cy = round(pwy + (phy - pwy) / diagonal * (diagonal / 2))
                    return int(r_cx), int(r_cy), int(r_width), int(r_height)
            else:
                pwx, pwy, phx, phy = self.__compute_vertex(p1x, p1y, p1x, p1y, p2x, p2y, p4x, p4y, width, height,
                                                           r_width, r_height)
                r_cx = round(pwx + (phx - pwx) / diagonal * (diagonal / 2))
                r_cy = round(pwy + (phy - pwy) / diagonal * (diagonal / 2))
                return int(r_cx), int(r_cy), int(r_width), int(r_height)
        flag, ix, iy = self.__segment_intersect_display(p2x, p2y, p3x, p3y)
        if flag:
            if height > 10000:
                if math.sqrt((ix - p2x) ** 2 + (iy - p2y) ** 2) < 5000:
                    pwx, pwy, phx, phy = self.__compute_vertex(p2x, p2y, p2x, p2y, p1x, p1y, p3x, p3y, width, height,
                                                               r_width, r_height)
                    r_cx = round(pwx + (phx - pwx) / diagonal * (diagonal / 2))
                    r_cy = round(pwy + (phy - pwy) / diagonal * (diagonal / 2))
                    return int(r_cx), int(r_cy), int(r_width), int(r_height)
                elif height - math.sqrt((ix - p2x) ** 2 + (iy - p2y) ** 2) < 5000:
                    pwx, pwy, phx, phy = self.__compute_vertex(p3x, p3y, p3x, p3y, p4x, p4y, p2x, p2y, width, height,
                                                               r_width, r_height)
                    r_cx = round(pwx + (phx - pwx) / diagonal * (diagonal / 2))
                    r_cy = round(pwy + (phy - pwy) / diagonal * (diagonal / 2))
                    return int(r_cx), int(r_cy), int(r_width), int(r_height)
                else:
                    sx = p2x + (p3x - p2x) / height * (math.sqrt((ix - p2x) ** 2 + (iy - p2y) ** 2) - 5000)
                    sy = p2y + (p3y - p2y) / height * (math.sqrt((ix - p2x) ** 2 + (iy - p2y) ** 2) - 5000)
                    pwx, pwy, phx, phy = self.__compute_vertex(sx, sy, p2x, p2y, p1x, p1y, p3x, p3y, width, height,
                                                               r_width, r_height)
                    r_cx = round(pwx + (phx - pwx) / diagonal * (diagonal / 2))
                    r_cy = round(pwy + (phy - pwy) / diagonal * (diagonal / 2))
                    return int(r_cx), int(r_cy), int(r_width), int(r_height)
            else:
                pwx, pwy, phx, phy = self.__compute_vertex(p2x, p2y, p2x, p2y, p1x, p1y, p3x, p3y, width, height,
                                                           r_width, r_height)
                r_cx = round(pwx + (phx - pwx) / diagonal * (diagonal / 2))
                r_cy = round(pwy + (phy - pwy) / diagonal * (diagonal / 2))
                return int(r_cx), int(r_cy), int(r_width), int(r_height)
        flag, ix, iy = self.__segment_intersect_display(p3x, p3y, p4x, p4y)
        if flag:
            if width > 10000:
                if math.sqrt((ix - p3x) ** 2 + (iy - p3y) ** 2) < 5000:
                    pwx, pwy, phx, phy = self.__compute_vertex(p3x, p3y, p3x, p3y, p4x, p4y, p2x, p2y, width, height,
                                                               r_width, r_height)
                    r_cx = round(pwx + (phx - pwx) / diagonal * (diagonal / 2))
                    r_cy = round(pwy + (phy - pwy) / diagonal * (diagonal / 2))
                    return int(r_cx), int(r_cy), int(r_width), int(r_height)
                elif width - math.sqrt((ix - p3x) ** 2 + (iy - p3y) ** 2) < 5000:
                    pwx, pwy, phx, phy = self.__compute_vertex(p4x, p4y, p4x, p4y, p3x, p3y, p1x, p1y, width, height,
                                                               r_width, r_height)
                    r_cx = round(pwx + (phx - pwx) / diagonal * (diagonal / 2))
                    r_cy = round(pwy + (phy - pwy) / diagonal * (diagonal / 2))
                    return int(r_cx), int(r_cy), int(r_width), int(r_height)
                else:
                    sx = p3x + (p4x - p3x) / width * (math.sqrt((ix - p3x) ** 2 + (iy - p3y) ** 2) - 5000)
                    sy = p3y + (p4y - p3y) / width * (math.sqrt((ix - p3x) ** 2 + (iy - p3y) ** 2) - 5000)
                    pwx, pwy, phx, phy = self.__compute_vertex(sx, sy, p3x, p3y, p4x, p4y, p2x, p2y, width, height,
                                                               r_width, r_height)
                    r_cx = round(pwx + (phx - pwx) / diagonal * (diagonal / 2))
                    r_cy = round(pwy + (phy - pwy) / diagonal * (diagonal / 2))
                    return int(r_cx), int(r_cy), int(r_width), int(r_height)
            else:
                pwx, pwy, phx, phy = self.__compute_vertex(p3x, p3y, p3x, p3y, p4x, p4y, p2x, p2y, width, height,
                                                           r_width, r_height)
                r_cx = round(pwx + (phx - pwx) / diagonal * (diagonal / 2))
                r_cy = round(pwy + (phy - pwy) / diagonal * (diagonal / 2))
                return int(r_cx), int(r_cy), int(r_width), int(r_height)
        flag, ix, iy = self.__segment_intersect_display(p4x, p4y, p1x, p1y)
        if flag:
            if height > 10000:
                if math.sqrt((ix - p4x) ** 2 + (iy - p4y) ** 2) < 5000:
                    pwx, pwy, phx, phy = self.__compute_vertex(p4x, p4y, p4x, p4y, p3x, p3y, p1x, p1y, width, height,
                                                               r_width, r_height)
                    r_cx = round(pwx + (phx - pwx) / diagonal * (diagonal / 2))
                    r_cy = round(pwy + (phy - pwy) / diagonal * (diagonal / 2))
                    return int(r_cx), int(r_cy), int(r_width), int(r_height)
                elif height - math.sqrt((ix - p4x) ** 2 + (iy - p4y) ** 2) < 5000:
                    pwx, pwy, phx, phy = self.__compute_vertex(p1x, p1y, p1x, p1y, p2x, p2y, p4x, p4y, width, height,
                                                               r_width, r_height)
                    r_cx = round(pwx + (phx - pwx) / diagonal * (diagonal / 2))
                    r_cy = round(pwy + (phy - pwy) / diagonal * (diagonal / 2))
                    return int(r_cx), int(r_cy), int(r_width), int(r_height)
                else:
                    sx = p4x + (p1x - p4x) / height * (math.sqrt((ix - p4x) ** 2 + (iy - p4y) ** 2) - 5000)
                    sy = p4y + (p1y - p4y) / height * (math.sqrt((ix - p4x) ** 2 + (iy - p4y) ** 2) - 5000)
                    pwx, pwy, phx, phy = self.__compute_vertex(sx, sy, p4x, p4y, p3x, p3y, p1x, p1y, width, height,
                                                               r_width, r_height)
                    r_cx = round(pwx + (phx - pwx) / diagonal * (diagonal / 2))
                    r_cy = round(pwy + (phy - pwy) / diagonal * (diagonal / 2))
                    return int(r_cx), int(r_cy), int(r_width), int(r_height)
            else:
                pwx, pwy, phx, phy = self.__compute_vertex(p4x, p4y, p4x, p4y, p3x, p3y, p1x, p1y, width, height,
                                                           r_width, r_height)
                r_cx = round(pwx + (phx - pwx) / diagonal * (diagonal / 2))
                r_cy = round(pwy + (phy - pwy) / diagonal * (diagonal / 2))
                return int(r_cx), int(r_cy), int(r_width), int(r_height)
        return 0, 0, 0, 0

    def __segment_intersect_display(self, l1x, l1y, l2x, l2y):
        if l2x > l1x:
            sx = l1x
            ex = l2x
        else:
            sx = l2x
            ex = l1x
        if l2y > l1y:
            sy = l1y
            ey = l2y
        else:
            sy = l2y
            ey = l1y
        if l2y - l1y == 0:
            lxb = 0
        else:
            lxb = (l2x - l1x) / (l2y - l1y)
        if l2x - l1x == 0:
            lyb = 0
        else:
            lyb = (l2y - l1y) / (l2x - l1x)
        if sy <= l1y + (0 - l1x) * lyb <= ey and 0 <= l1y + (0 - l1x) * lyb <= self.__display_height:
            return True, 0, l1y + (0 - l1x) * lyb
        if sy <= l1y + (self.__display_width - l1x) * lyb <= ey and 0 <= l1y + (
                self.__display_width - l1x) * lyb <= self.__display_height:
            return True, self.__display_width, l1y + (self.__display_width - l1x) * lyb
        if sx <= l1x + (0 - l1y) * lxb <= ex and 0 <= l1x + (0 - l1y) * lxb <= self.__display_width:
            return True, l1x + (0 - l1y) * lxb, 0
        if sx <= l1x + (self.__display_height - l1y) * lxb <= ex and 0 <= l1x + (
                self.__display_height - l1y) * lxb <= self.__display_width:
            return True, l1x + (self.__display_height - l1y) * lxb, self.__display_height
        return False, 0, 0

    @staticmethod
    def __compute_vertex(sx, sy, jx, jy, wx, wy, hx, hy, w, h, rw, rh):
        pwx = sx + (wx - jx) / w * rw
        pwy = sy + (wy - jy) / w * rw
        phx = sx + (hx - jx) / h * rh
        phy = sy + (hy - jy) / h * rh
        return pwx, pwy, phx, phy

    @staticmethod
    def __sin(x):
        return sp.sin(x * sp.pi / 180)

    @staticmethod
    def __cos(x):
        return sp.cos(x * sp.pi / 180)

    @staticmethod
    def __img_cover(src1, src2, clip=0):
        rows, cols, channels = src2.shape
        roi2 = src2[0:rows, 0:cols]
        if clip == 1:
            src1_2gray = cv2.cvtColor(src1, cv2.COLOR_BGR2GRAY)
            ret1, mask1 = cv2.threshold(src1_2gray, 1, 255, cv2.THRESH_BINARY_INV)
            image_bg1 = cv2.bitwise_and(roi2, roi2, mask=mask1)
            src2 = cv2.subtract(src2, image_bg1)
        B1, G1, R1 = cv2.split(src1)
        zeros = np.zeros(src1.shape[:2], dtype="uint8")
        src1 = cv2.merge([B1, zeros, R1])
        roi1 = src1[0:rows, 0:cols]
        B2, G2, R2 = cv2.split(src2)
        src2 = cv2.merge([B2, zeros, R2])
        src2_2gray = cv2.cvtColor(src2, cv2.COLOR_BGR2GRAY)
        ret2, mask2 = cv2.threshold(src2_2gray, 1, 255, cv2.THRESH_BINARY)
        image_bg = cv2.bitwise_and(roi1, roi1, mask=mask2)
        image = cv2.subtract(src1, image_bg)
        image = cv2.add(image, src2)
        return image

    def click(self, delay: int = 0) -> bool:
        if self.node is not None:
            self.device.click(Point(self.__center_x_to_global, self.__center_y_to_global), delay)
        return False

    def click_exist(self, timeout: int = None) -> bool:
        if self.exist(timeout):
            if (self.rect[len(self.rect) - 1][1] - self.rect[0][1] + 1) \
                    * (self.rect[len(self.rect) - 1][0] - self.rect[0][0] + 1) == len(self.rect):
                x = self.rect[0][1] + int((self.rect[len(self.rect) - 1][1] - self.rect[0][1] + 1) / 2)
                y = self.rect[0][0] + int((self.rect[len(self.rect) - 1][0] - self.rect[0][0] + 1) / 2)
                self.device.click(Point(x, y))
                return True
            self.device.click(Point(self.rect[100][1], self.rect[100][0]))
            return True
        return False

    def submit_string(self, text: str) -> bool:
        self.click()
        return self.device.submit_string(text)

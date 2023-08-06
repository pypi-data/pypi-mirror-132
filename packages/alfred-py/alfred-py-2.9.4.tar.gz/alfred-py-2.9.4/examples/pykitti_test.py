#
# Copyright (c) 2020 JinTian.
#
# This file is part of alfred
# (see http://jinfagang.github.io).
#
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
#
import pykitti
import cv2
import numpy as np
from alfred.vis.pointcloud.pointcloud_vis import draw_pcs_open3d


base_dir = '/media/jintain/sg/permanent/datasets/KITTI/videos'
date = '2011_09_26'
drive = '0051'

data = pykitti.raw(base_dir, date, drive)
print(data.cam2_files)
cam2_img = data.get_rgb(3)[1]
print(cam2_img)
cv2.imshow('rr', np.array(cam2_img))

# data.calib.T_cam0_velo.dot(point_velo)
res = [[12.189727, 4.65575, -1.0090133, 1.6713146, 3.9860756, 1.4752198, 1.4311914],
       [7.0290184, 18.43234, -1.0616484, 1.5949062, 3.7942128, 1.4587526, 0.03434156],
       [9.716782, 18.663864, -1.081424, 1.6270422, 4.0220504, 1.428338, 0.010275014],
       [12.390503, 18.554394, -1.0709403, 1.5716408, 3.8583813, 1.4068353, 0.092568964],
       [9.162392, -3.2395134, -0.9900443, 0.48879692, 1.7805163, 1.780584, 4.7180395],
       [1.5449369, 19.820513, -1.1250883, 1.61444, 4.0291963, 1.4679328, 0.20142984],
       [15.010401, 17.861265, -0.61177015, 1.8016329, 4.52904, 1.9179995, -0.0009133518],
       [0.2915942, 14.302571, -1.6358033, 0.6031256, 1.7338636, 1.693197, 2.0567284],
       [32.58985, 16.622143, -0.9154575, 1.56024, 3.6420622, 1.4507264, 1.5841204],
       [10.96289, 33.31957, -1.8625767, 1.6718575, 4.1056437, 1.5355072, -0.5065325],
       [-20.711775, 12.870968, -1.3916719, 0.6494945, 0.6588189, 1.7635618, 2.878424],
       [-14.706663, 14.144306, -1.4347086, 0.5646943, 1.7102921, 1.7303042, 1.6427889],
       [-34.937218, -32.419926, -1.9705622, 2.0217955, 6.3850527, 2.5362377, 0.9260524],
       [-25.85193, 13.433075, -1.6172849, 0.5029159, 1.7657202, 1.6948656, 1.8433876],
       [-8.7119255, 15.603356, -0.861634, 0.61332655, 1.7866454, 1.7575798, -0.15929039],
       [0.44268692, -31.126797, -1.4658432, 0.6214817, 1.778398, 1.6685283, 2.7185097],
       [-1.3864591, 43.80352, -1.6687126, 1.990596, 5.726587, 2.5764484, 0.53529406],
       [-46.30665, -24.680546, -1.5553175, 0.54056036, 1.8155692, 1.7282323, 1.4364488],
       [-25.206638, 14.19597, -1.6388608, 0.60298264, 0.6539766, 1.7206633, 2.6259918],
       [42.099804, 16.609531, -0.95861834, 1.6101078, 3.805344, 1.5348499, 1.4423454]]

for p in res:
    pts3d_c = p[:3]
    cam0_xyz = data.calib.Tr

cv2.waitKey(0)
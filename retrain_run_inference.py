
"""Inception v3 architecture 모델을 retraining한 모델을 이용해서 이미지에 대한 추론(inference)을 진행하는 예제"""

import numpy as np
import tensorflow as tf
import Get_and_Split_path

#PATH = Get_and_Split_path.RETRAIN_PATH


# 추론을 진행할 이미지 경로
#imagePath = Get_and_Split_path.FILE_PATH         ###########옷을 업로드 할때 그 해당 링크
# 읽어들일 graph 파일 경로
#modelFullPath = PATH + '/output_graph.pb'
# 읽어들일 labels 파일 경로
#labelsFullPath = PATH + '/output_labels.txt'

class retrain_run_inference:
    def __init__(self, get_all_path):
        self.PATH = get_all_path.RETRAIN_PATH
        # 추론을 진행할 이미지 경로
        self.imagePath = get_all_path.FILE_PATH
        # 읽어들일 graph 파일 경로
        self.modelFullPath = self.PATH + '/output_graph.pb'
        # 읽어들일 labels 파일 경로
        self.labelsFullPath = self.PATH + '/output_labels.txt'

    def create_graph(self):
        """저장된(saved) GraphDef 파일로부터 graph를 생성하고 saver를 반환한다."""
        # 저장된(saved) graph_def.pb로부터 graph를 생성한다.
        with tf.gfile.FastGFile(self.modelFullPath, 'rb') as f:
            graph_def = tf.GraphDef()
            graph_def.ParseFromString(f.read())
            _ = tf.import_graph_def(graph_def, name='')


    def run_inference_on_image(self):
        answer = None

        if not tf.gfile.Exists(self.imagePath):
            tf.logging.fatal('File does not exist %s', self.imagePath)
            return answer

        image_data = tf.gfile.FastGFile(self.imagePath, 'rb').read()

        # 저장된(saved) GraphDef 파일로부터 graph를 생성한다.
        self.create_graph()

        with tf.Session() as sess:

            softmax_tensor = sess.graph.get_tensor_by_name('final_result:0')
            predictions = sess.run(softmax_tensor,
                                   {'DecodeJpeg/contents:0': image_data})
            predictions = np.squeeze(predictions)

            top_k = predictions.argsort()[-5:][::-1]  # 가장 높은 확률을 가진 5개(top 5)의 예측값(predictions)을 얻는다.
            f = open(self.labelsFullPath, 'rb')
            lines = f.readlines()
            labels = [str(w).replace("\n", "") for w in lines]
            for node_id in top_k:
                human_string = labels[node_id]
                score = predictions[node_id]
                print('%s (score = %.5f)' % (human_string, score))

            answer = labels[top_k[0]]

            return answer


if __name__ == '__main__':
    retrain_run_inference = retrain_run_inference()
    retrain_run_inference.run_inference_on_image()
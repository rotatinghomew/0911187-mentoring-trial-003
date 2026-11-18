# 导师指导试点分析

本项目整理指导试点中的方案邀请、实际指导活动、学生转组或暂停以及研究结果。每条事件有稳定 `id`、`student_id`、事件类型和日期；`offered` 表示最初分配，`session` 记录实际接受的指导，两者不代表同一暴露。

输入为本地合成 UTF-8 JSON 数组。日期使用 ISO 8601 格式，`outcome` 事件可包含数值 `value`。缺少结果的学生会列入随访缺失清单，不作为零结果。当前报告按学生呈现事件轨迹，不对非随机试点作因果承诺，也不保存提交后的历史比较版本。

需要 Python 3.11 或更新版本，无外部服务。执行 `PYTHONPATH=src python -m unittest discover -s tests -v` 运行测试。`mentoring_trial.facts` 校验事件，`mentoring_trial.exposure.histories` 重建指导经历，`mentoring_trial.analysis.summarize` 汇总邀请、参与和随访，`mentoring_trial.reports.build_report` 输出带数据修订号的报告。样例见 `examples/sample.json`。

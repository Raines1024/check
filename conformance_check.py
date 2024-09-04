import pm4py
import sys


if __name__ == "__main__":

    # 加载 .xes 文件
    BPIC13_i = pm4py.read_xes('BPIC13_i.xes')
    BPIC13_cp = pm4py.read_xes('BPIC13_cp.xes')
    BPIC15_1f = pm4py.read_xes("BPIC15_1f.xes")
    BPIC15_2f = pm4py.read_xes("BPIC15_2f.xes")
    BPIC15_4f = pm4py.read_xes("BPIC15_4f.xes")
    BPIC15_5f = pm4py.read_xes("BPIC15_5f.xes")


    if len(sys.argv) > 1:
        # 获取第一个命令行参数
        param = sys.argv[1]
        print(f"第一个命令行参数是: {param}")
        if param == "fitness_token":
            # 使用基于令牌的重放来计算适应度
            net_1, im_1, fm_1 = pm4py.discover_petri_net_inductive(BPIC13_i, activity_key='concept:name',
                                                             case_id_key='case:concept:name',
                                                             timestamp_key='time:timestamp')
            fitness_tbr = pm4py.fitness_token_based_replay(BPIC13_i, net_1, im_1, fm_1, activity_key='concept:name',
                                                           case_id_key='case:concept:name',
                                                           timestamp_key='time:timestamp')
            net_2, im_2, fm_2 = pm4py.discover_petri_net_inductive(BPIC13_cp, activity_key='concept:name',
                                                                   case_id_key='case:concept:name',
                                                                   timestamp_key='time:timestamp')
            fitness_tbr = pm4py.fitness_token_based_replay(BPIC13_cp, net_2, im_2, fm_2, activity_key='concept:name',
                                                           case_id_key='case:concept:name',
                                                           timestamp_key='time:timestamp')
            net_3, im_3, fm_3 = pm4py.discover_petri_net_inductive(BPIC15_1f, activity_key='concept:name',
                                                                   case_id_key='case:concept:name',
                                                                   timestamp_key='time:timestamp')
            fitness_tbr = pm4py.fitness_token_based_replay(BPIC15_1f, net_3, im_3, fm_3, activity_key='concept:name',
                                                           case_id_key='case:concept:name',
                                                           timestamp_key='time:timestamp')
            net_4, im_4, fm_4 = pm4py.discover_petri_net_inductive(BPIC15_2f, activity_key='concept:name',
                                                                   case_id_key='case:concept:name',
                                                                   timestamp_key='time:timestamp')
            fitness_tbr = pm4py.fitness_token_based_replay(BPIC15_2f, net_4, im_4, fm_4, activity_key='concept:name',
                                                           case_id_key='case:concept:name',
                                                           timestamp_key='time:timestamp')
            net_5, im_5, fm_5 = pm4py.discover_petri_net_inductive(BPIC15_4f, activity_key='concept:name',
                                                                   case_id_key='case:concept:name',
                                                                   timestamp_key='time:timestamp')
            fitness_tbr = pm4py.fitness_token_based_replay(BPIC15_4f, net_5, im_5, fm_5, activity_key='concept:name',
                                                           case_id_key='case:concept:name',
                                                           timestamp_key='time:timestamp')
            net_6, im_6, fm_6 = pm4py.discover_petri_net_inductive(BPIC15_5f, activity_key='concept:name',
                                                                   case_id_key='case:concept:name',
                                                                   timestamp_key='time:timestamp')
            fitness_tbr = pm4py.fitness_token_based_replay(BPIC15_5f, net_6, im_6, fm_6, activity_key='concept:name',
                                                           case_id_key='case:concept:name',
                                                           timestamp_key='time:timestamp')

        elif param == "precision_token":
            # 使用基于令牌的重放计算精度
            net_1, im_1, fm_1 = pm4py.discover_petri_net_inductive(BPIC13_i, activity_key='concept:name',
                                                                   case_id_key='case:concept:name',
                                                                   timestamp_key='time:timestamp')
            precision_tbr = pm4py.precision_token_based_replay(BPIC13_i, net_1, im_1, fm_1, activity_key='concept:name',
                                                          case_id_key='case:concept:name',
                                                          timestamp_key='time:timestamp')
            net_2, im_2, fm_2 = pm4py.discover_petri_net_inductive(BPIC13_cp, activity_key='concept:name',
                                                                   case_id_key='case:concept:name',
                                                                   timestamp_key='time:timestamp')
            precision_tbr = pm4py.precision_token_based_replay(BPIC13_cp, net_2, im_2, fm_2, activity_key='concept:name',
                                                          case_id_key='case:concept:name',
                                                          timestamp_key='time:timestamp')
            net_3, im_3, fm_3 = pm4py.discover_petri_net_inductive(BPIC15_1f, activity_key='concept:name',
                                                                   case_id_key='case:concept:name',
                                                                   timestamp_key='time:timestamp')
            precision_tbr = pm4py.precision_token_based_replay(BPIC15_1f, net_3, im_3, fm_3, activity_key='concept:name',
                                                          case_id_key='case:concept:name',
                                                          timestamp_key='time:timestamp')
            net_4, im_4, fm_4 = pm4py.discover_petri_net_inductive(BPIC15_2f, activity_key='concept:name',
                                                                   case_id_key='case:concept:name',
                                                                   timestamp_key='time:timestamp')
            precision_tbr = pm4py.precision_token_based_replay(BPIC15_2f, net_4, im_4, fm_4, activity_key='concept:name',
                                                          case_id_key='case:concept:name',
                                                          timestamp_key='time:timestamp')
            net_5, im_5, fm_5 = pm4py.discover_petri_net_inductive(BPIC15_4f, activity_key='concept:name',
                                                                   case_id_key='case:concept:name',
                                                                   timestamp_key='time:timestamp')
            precision_tbr = pm4py.precision_token_based_replay(BPIC15_4f, net_5, im_5, fm_5, activity_key='concept:name',
                                                          case_id_key='case:concept:name',
                                                          timestamp_key='time:timestamp')
            net_6, im_6, fm_6 = pm4py.discover_petri_net_inductive(BPIC15_5f, activity_key='concept:name',
                                                                   case_id_key='case:concept:name',
                                                                   timestamp_key='time:timestamp')
            precision_tbr = pm4py.precision_token_based_replay(BPIC15_5f, net_6, im_6, fm_6, activity_key='concept:name',
                                                          case_id_key='case:concept:name',
                                                          timestamp_key='time:timestamp')
        elif param == "conformance_log_skeleton":
            # 使用日志框架执行一致性检查
            log_skeleton_1 = pm4py.discover_log_skeleton(BPIC13_i, noise_threshold=0.1, activity_key='concept:name',
                                                       case_id_key='case:concept:name', timestamp_key='time:timestamp')
            conformance_lsk = pm4py.conformance_log_skeleton(BPIC13_i, log_skeleton_1, activity_key='concept:name',
                                                             case_id_key='case:concept:name',
                                                             timestamp_key='time:timestamp')
            log_skeleton_2 = pm4py.discover_log_skeleton(BPIC13_cp, noise_threshold=0.1, activity_key='concept:name',
                                                         case_id_key='case:concept:name',
                                                         timestamp_key='time:timestamp')
            conformance_lsk = pm4py.conformance_log_skeleton(BPIC13_cp, log_skeleton_2, activity_key='concept:name',
                                                             case_id_key='case:concept:name',
                                                             timestamp_key='time:timestamp')
            log_skeleton_3 = pm4py.discover_log_skeleton(BPIC15_1f, noise_threshold=0.1, activity_key='concept:name',
                                                         case_id_key='case:concept:name',
                                                         timestamp_key='time:timestamp')
            conformance_lsk = pm4py.conformance_log_skeleton(BPIC15_1f, log_skeleton_3, activity_key='concept:name',
                                                             case_id_key='case:concept:name',
                                                             timestamp_key='time:timestamp')
            log_skeleton_4 = pm4py.discover_log_skeleton(BPIC15_2f, noise_threshold=0.1, activity_key='concept:name',
                                                         case_id_key='case:concept:name',
                                                         timestamp_key='time:timestamp')
            conformance_lsk = pm4py.conformance_log_skeleton(BPIC15_2f, log_skeleton_4, activity_key='concept:name',
                                                             case_id_key='case:concept:name',
                                                             timestamp_key='time:timestamp')
            log_skeleton_5 = pm4py.discover_log_skeleton(BPIC15_4f, noise_threshold=0.1, activity_key='concept:name',
                                                         case_id_key='case:concept:name',
                                                         timestamp_key='time:timestamp')
            conformance_lsk = pm4py.conformance_log_skeleton(BPIC15_4f, log_skeleton_5, activity_key='concept:name',
                                                             case_id_key='case:concept:name',
                                                             timestamp_key='time:timestamp')
            log_skeleton_6 = pm4py.discover_log_skeleton(BPIC15_5f, noise_threshold=0.1, activity_key='concept:name',
                                                         case_id_key='case:concept:name',
                                                         timestamp_key='time:timestamp')
            conformance_lsk = pm4py.conformance_log_skeleton(BPIC15_5f, log_skeleton_6, activity_key='concept:name',
                                                             case_id_key='case:concept:name',
                                                             timestamp_key='time:timestamp')
        elif param == "conformance_declare":
            # 对 DECLARE 模型应用一致性检查
            declare_model_1 = pm4py.discover_declare(BPIC13_i)
            conf_result = pm4py.conformance_declare(BPIC13_i, declare_model_1)

            declare_model_2 = pm4py.discover_declare(BPIC13_cp)
            conf_result = pm4py.conformance_declare(BPIC13_cp, declare_model_2)

            declare_model_3 = pm4py.discover_declare(BPIC15_1f)
            conf_result = pm4py.conformance_declare(BPIC15_1f, declare_model_3)

            declare_model_4 = pm4py.discover_declare(BPIC15_2f)
            conf_result = pm4py.conformance_declare(BPIC15_2f, declare_model_4)

            declare_model_5 = pm4py.discover_declare(BPIC15_4f)
            conf_result = pm4py.conformance_declare(BPIC15_4f, declare_model_5)

            declare_model_6 = pm4py.discover_declare(BPIC15_5f)
            conf_result = pm4py.conformance_declare(BPIC15_5f, declare_model_6)


        elif param == "conformance_temporal_profile":
            # 对提供的日志与提供的时间配置文件执行一致性检查
            temporal_profile_1 = pm4py.discover_temporal_profile(BPIC13_i, activity_key='concept:name',
                                                               case_id_key='case:concept:name',
                                                               timestamp_key='time:timestamp')
            conformance_temporal_profile = pm4py.conformance_temporal_profile(BPIC13_i, temporal_profile_1, zeta=1,
                                                                              activity_key='concept:name',
                                                                              case_id_key='case:concept:name',
                                                                              timestamp_key='time:timestamp')
            temporal_profile_2 = pm4py.discover_temporal_profile(BPIC13_cp, activity_key='concept:name',
                                                                 case_id_key='case:concept:name',
                                                                 timestamp_key='time:timestamp')
            conformance_temporal_profile = pm4py.conformance_temporal_profile(BPIC13_cp, temporal_profile_2, zeta=1,
                                                                              activity_key='concept:name',
                                                                              case_id_key='case:concept:name',
                                                                              timestamp_key='time:timestamp')
            temporal_profile_3 = pm4py.discover_temporal_profile(BPIC15_1f, activity_key='concept:name',
                                                                 case_id_key='case:concept:name',
                                                                 timestamp_key='time:timestamp')
            conformance_temporal_profile = pm4py.conformance_temporal_profile(BPIC15_1f, temporal_profile_3, zeta=1,
                                                                              activity_key='concept:name',
                                                                              case_id_key='case:concept:name',
                                                                              timestamp_key='time:timestamp')
            temporal_profile_4 = pm4py.discover_temporal_profile(BPIC15_2f, activity_key='concept:name',
                                                                 case_id_key='case:concept:name',
                                                                 timestamp_key='time:timestamp')
            conformance_temporal_profile = pm4py.conformance_temporal_profile(BPIC15_2f, temporal_profile_4, zeta=1,
                                                                              activity_key='concept:name',
                                                                              case_id_key='case:concept:name',
                                                                              timestamp_key='time:timestamp')
            temporal_profile_5 = pm4py.discover_temporal_profile(BPIC15_4f, activity_key='concept:name',
                                                                 case_id_key='case:concept:name',
                                                                 timestamp_key='time:timestamp')
            conformance_temporal_profile = pm4py.conformance_temporal_profile(BPIC15_4f, temporal_profile_5, zeta=1,
                                                                              activity_key='concept:name',
                                                                              case_id_key='case:concept:name',
                                                                              timestamp_key='time:timestamp')
            temporal_profile_6 = pm4py.discover_temporal_profile(BPIC15_5f, activity_key='concept:name',
                                                                 case_id_key='case:concept:name',
                                                                 timestamp_key='time:timestamp')
            conformance_temporal_profile = pm4py.conformance_temporal_profile(BPIC15_5f, temporal_profile_6, zeta=1,
                                                                              activity_key='concept:name',
                                                                              case_id_key='case:concept:name',
                                                                              timestamp_key='time:timestamp')
    else:
        print("没有提供任何命令行参数")



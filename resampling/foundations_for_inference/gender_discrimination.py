
# pandas standard library
import sys

# third-party
import pandas
import matplotlib
import matplotlib.pyplot as plot

matplotlib.style.use('ggplot')

GENDER_COUNT = 24
MALES_PROMOTED = 21
FEMALES_PROMOTED = 14
GENDER_DIFFERENCE = MALES_PROMOTED - FEMALES_PROMOTED
FEMALES_NOT_PROMOTED = GENDER_COUNT - FEMALES_PROMOTED
MALES_NOT_PROMOTED = GENDER_COUNT - MALES_PROMOTED

experiment_data = pandas.DataFrame({"Promoted": [MALES_PROMOTED,
                                                 FEMALES_PROMOTED],
                                    "Not Promoted": [MALES_NOT_PROMOTED,
                                                     FEMALES_NOT_PROMOTED]},
                                   index='male female'.split(),
                                   columns=["Promoted", "Not Promoted"])

experiment_frame = experiment_data.copy()
experiment_frame['Total'] = sum((experiment_frame[column] for column in
                                 experiment_frame.columns))
last_row = pandas.DataFrame(experiment_frame.sum()).transpose()
last_row.index = pandas.Index(['Total'])
experiment_frame = pandas.concat((experiment_frame, last_row))

class IndentOutput(object):
    """Fake file output for csv-writing """
    @classmethod
    def write(cls, line):
        """Write line to stdout with three spaces prepended"""
        sys.stdout.write("   {0}".format(line))

print('.. csv-table:: Experiment Outcome')
print('   :header: ,{0}\n'.format(','.join(experiment_frame.columns)))

experiment_frame.to_csv(IndentOutput, header=False)

print('.. csv-table:: Experiment proportions')
print('   :header: ,{0}\n'.format(','.join(experiment_frame.columns)))

totals = pandas.Series([GENDER_COUNT, GENDER_COUNT, GENDER_COUNT * 2],
                       index='male female Total'.split())
total_frame = pandas.DataFrame({'Promoted': totals,
                                "Not Promoted": totals,
                                "Total": totals})
proportions = experiment_frame/total_frame
proportions.to_csv(IndentOutput, header=False,
                   columns=['Promoted', 'Not Promoted', 'Total'],
                   float_format="%.3f")

path = 'figures/gender_experiment_bar.svg'
figure = plot.figure()
axe = figure.gca()
experiment_data.plot(kind='bar', ax=axe)
figure.savefig(path)
print('.. image:: {0}'.format(path))

print("   \\frac{{{0}}}{{{2}}}- \\frac{{{1}}}{{{2}}}&=\\frac{{{3}}}{{{2}}}\\\\".format(MALES_PROMOTED,
                                                                                   FEMALES_PROMOTED,
                                                                                   GENDER_COUNT,
                                                                                   GENDER_DIFFERENCE))
print("   &\\approx {:.3f}\\\\".format(GENDER_DIFFERENCE/GENDER_COUNT))

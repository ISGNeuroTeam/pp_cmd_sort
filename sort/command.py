from otlang.sdk.syntax import Positional, Keyword, OTLType
from pp_exec_env.base_command import BaseCommand, Syntax, pd


def _sort(df: pd.DataFrame, field: list[str], ascending: bool) -> None:
    df.sort_values(field, ascending=ascending, inplace=True)


DEFAULT_NUMBER = 10


class SortCommand(BaseCommand):
    syntax = Syntax(
        [
            Positional("clause", required=False, otl_type=OTLType.STRING),
            Keyword("count", required=False, otl_type=OTLType.INTEGER)
        ],
    )

    def transform(self, df: pd.DataFrame) -> pd.DataFrame:
        clause = self.get_arg("clause").group_by
        direction = self.get_arg("clause").value
        if direction == '+' or 'asc':
            _sort(df, field=clause, ascending=True)
        elif direction == '-' or 'des':
            _sort(df, field=clause, ascending=False)
        else:
            raise TypeError
        return df.head(self.get_arg("count").value or DEFAULT_NUMBER)

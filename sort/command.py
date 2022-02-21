from pp_exec_env.base_command import BaseCommand, Syntax, Rule, pd


def _sort(df: pd.DataFrame, field: str, ascending: bool) -> None:
    df.sort_values(field, ascending=ascending)


class SortCommand(BaseCommand):
    syntax = Syntax([Rule(name="direction", type="arg", input_types=['string', 'term'], inf=True)],
                    use_timewindow=False)

    def transform(self, df: pd.DataFrame) -> pd.DataFrame:
        for direction in self.get_arg('direction'):
            if direction.value.lower() == 'asc':
                for field in direction.group_by:
                    _sort(df, field=field, ascending=True)
            elif direction.value.lower() == 'desc':
                for field in direction.group_by:
                    _sort(df, field=field, ascending=False)
            else:
                raise Exception
        return df

.headers on
.mode csv
.output /Users/pdesl/PycharmProjects/GeneticInvesting/data.csv
select title,
  amount_invested,
  profit,
  date_start,
  date_end,
  confirmation_of_investment,
  confirmation_of_withdrawal from investment;
select name,
  alias from title;
.quit

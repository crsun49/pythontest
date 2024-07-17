
CREATE TABLE [dbo].[p_zhixingfuye](
    [id] [uniqueidentifier] NOT NULL,
    [title] [nvarchar](200) NULL,
    [src] [varchar](max) NULL,
    [img] [nvarchar](200) NULL,
    [context] [nvarchar](max) NULL,
    [status] [tinyint] NULL,
    [createtime] [datetime] NULL,
    [filepath] [nvarchar](50) NULL
    ) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
    GO
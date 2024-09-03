

drop table p_xbgame

CREATE TABLE [dbo].[p_xbgame](
    [id] [uniqueidentifier] NOT NULL,
    [title] [nvarchar](200) NULL,
    [gameName] [nvarchar](200) NULL,
    [gameNameCh] [nvarchar](200) NULL,
    [href] [varchar](max) NULL,
    [filename] [nvarchar](200) NULL,
    [imgsrc] [nvarchar](200) NULL,
    [videosrc] [nvarchar](200) NULL,
    [gameintroduce] [nvarchar](max) NULL,
    [status] [tinyint] NULL,
    [isTs] [tinyint] NULL,
    [errorMsg] [varchar](max) NULL,
    [createtime] [datetime] NULL,
    [imgFilePath] [nvarchar](200) NULL,
    [videoFilePath] [nvarchar](200) NULL
    ) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
    GO



